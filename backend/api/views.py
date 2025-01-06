from django.shortcuts import render
from django.http import JsonResponse

def decompose_word(request):
	word = request.GET.get('word', '')
	components = ["example", "decomposition"]
	return JsonResponse({'word': word, 'components': components})
