from django.shortcuts import render
from django.http import JsonResponse
from zemberek import TurkishMorphology
import re, os

LANGUAGES = {
	"Turkish": "tr",
}

morphology = TurkishMorphology.create_with_defaults()

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

	print("Performing regex on this string: " + interpretation[1])
	word_feat = r"(\w+:(?:\w+→\w+|\w+))" # word:feature or word:feature->feature
	pattern = r"{}(?:\+{})*(?:\|{})?".format(word_feat, word_feat, word_feat)

	regex_matches = re.findall(pattern, interpretation[1])
	dict = {}
	for match in regex_matches:
		for elem in match:
			if elem:
				elem = elem.split(':')
				dict[elem[0]] = elem[1]
	print(dict)

	path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	path = os.path.join(path, 'human_readable_features.txt')
	human_readable_file = open(path)

	# match each feature with feature value name and output a human readable description/blurb

	human_readable_file.close()
	
