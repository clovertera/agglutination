from django.shortcuts import render
from django.http import JsonResponse
from zemberek import TurkishMorphology

LANGUAGES = {
	"Turkish": "tr",
}

morphology = TurkishMorphology.create_with_defaults()

def decompose_word(request):
	word = request.GET.get('word', '')
	language = request.GET.get('language', '')
	# need to use stanza to get the components of the requested word
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
	return results_list