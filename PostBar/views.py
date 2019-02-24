from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage':"How's the day"}
    return render(request, 'PostBar/index.html', context=context_dict)

def about(request):
	context_dict = {'boldmessage':"Zhouyang shen    ,   Yixuan Dai   ,   Ming Ho Wu"}
	return render(request, 'PostBar/about.html', context=context_dict)