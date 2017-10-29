from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	context_dict={'boldmessage':"I am bold font from the context"}
	return render(request,'myrango/index.html',context_dict)
def about(request):
	response=HttpResponse()
	response.write("<p>Here's the text of the about page<p>")
	response.write("<a href=/myrango/>Index</a>")
	return response


# Create your views here.
