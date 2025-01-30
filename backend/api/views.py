from django.shortcuts import render
from django.http import JsonResponse
from zemberek import TurkishMorphology

LANGUAGES = {
	"Turkish": "tr",
}

def decompose_word(request):
	word = request.GET.get('word', '')
	language = request.GET.get('language', '')
	# need to use stanza to get the components of the requested word
	# use the given language
	components = ["example", "decomposition"]
	return JsonResponse({'word': word, 'components': components, 'language': language})

def get_components(word, language):
	# use zemberek
	print("zemberek")
	results = morphology.analyze("kalemin")
	for result in results:
		print(result)
	print("\n")
