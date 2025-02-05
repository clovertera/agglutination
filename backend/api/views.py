from django.shortcuts import render
from django.http import JsonResponse
from zemberek import TurkishMorphology
import re, os

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
	return JsonResponse({'word': word, 'components': components, 'language': language})

def get_components(word, language):
	# use zemberek
	results = morphology.analyze(word)
	results_list = []
	for result in results:
		results_list.append(str(result))
		make_human_readable(str(result))
	return results_list

def make_human_readable(interpretation):
	# interpretation example: 
	# [kalem:Noun] kalem:Noun+A3sg+in:Gen

	interpretation = re.split(r'[\[\]]+', interpretation)
	interpretation = [word for word in interpretation if word]
	interpretation[1] = interpretation[1].lstrip()

	#print("Performing regex on this string: " + interpretation[1])
	word_feat = r"(\w+:(?:\w+→\w+|\w+))" # word:feature or word:feature->feature
	pattern = r"{}(?:\+{})*(?:\|{})?".format(word_feat, word_feat, word_feat)

	# TODO: add regex capability for solo parts like A3sg? maybe?
	regex_matches = re.findall(pattern, interpretation[1])
	#print("matches")
	#print(regex_matches)
	feat_dict = {}
	for match in regex_matches:
		for elem in match:
			if elem:
				elem = elem.split(':')
				feat_dict[elem[0]] = elem[1]
				
	# TODO: IMPORTANT: add basic parts of speech (noun, verb etc) and stem
	# TODO: implement faster lookup. this is TEMPORARY

	# match each feature with feature value name and output a human readable description/blurb
	
	# TODO: formatting for each entry
	#print(feat_dict)
	for key, value in feat_dict.items():
		if value in total_dict:
			print(f"{key} : {value} ... {total_dict[value]}")
	
