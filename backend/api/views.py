from django.shortcuts import render
from django.http import JsonResponse
from zemberek import TurkishMorphology
import re, os, json

LANGUAGES = {
	"Turkish": "tr",
}

morphology = TurkishMorphology.create_with_defaults()
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
deriv_path = os.path.join(path, 'feature_descriptions_derivation.txt')
inflec_path = os.path.join(path, 'feature_descriptions_inflectional.txt')

# create lists of lists (each nested list is a key and its description)
with open(deriv_path) as deriv:
	deriv_text = [line.strip().split("\t") for line in deriv]

with open(inflec_path) as inflec:
	inflec_text = [line.strip().split("\t") for line in inflec]

total_dict = {}
for pair in deriv_text:
	total_dict[pair[0]] = pair[1]
for pair in inflec_text:
	total_dict[pair[0]] = pair[1]

def decompose_word(request):
	word = request.GET.get('word', '')
	language = request.GET.get('language', '')
	# need to use zemberek to get the components of the requested word
	# use the given language
	# placeholder: components = ["example", "decomposition"]
	components = get_components(word, 'Turkish')
	# this is a bit bulky
	return JsonResponse({'word': word, 'components': components, 'language': language})

def get_components(word, language):
	# use zemberek
	results = morphology.analyze(word)
	results_list = []
	for result in results:
		results_list.append(make_human_readable(str(result)))
	return results_list

def make_human_readable(interpretation):
	# interpretation example: 
	# [kalem:Noun] kalem:Noun+A3sg+in:Gen

	interpretation_split = re.split(r'[\[\]]+', interpretation)
	interpretation_split = [word for word in interpretation_split if word]
	interpretation_split[1] = interpretation_split[1].lstrip()

	#print("Performing regex on this string: " + interpretation[1])
	word_feat = r"(\w+:(?:\w+→\w+|\w+))" # word:feature or word:feature->feature
	pattern = r"{}(?:\+{})*(?:\|{})?".format(word_feat, word_feat, word_feat)

	# TODO: add regex capability for solo parts like A3sg? maybe?
	regex_matches = re.findall(pattern, interpretation_split[1])
	#print("matches")
	#print(regex_matches)
	dicts = []
	for match in regex_matches:
		feat_dict = {}
		for elem in match:
			if elem:
				elem = elem.split(':')
				if elem[1] in total_dict:
					feat_desc_list = [elem[1], total_dict[elem[1]]]
					feat_dict[elem[0]] = feat_desc_list
				else:
					feat_dict[elem[0]] = elem[1]
		dicts.append(feat_dict)
				
	print(dicts)
	# TODO: IMPORTANT: add basic parts of speech (noun, verb etc) and stem
	# TODO: implement faster lookup. this is TEMPORARY

	# match each feature with feature value name and output a human readable description/blurb
	
	# TODO: formatting for each entry
	
	# convert to JSON object for easy frontend
	json_output = {
		"zemberek_analysis":interpretation, 
		"morphological_features": dicts
	}
	return(json_output)