from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Rango says: Hello world! <br/> <a href=/myrango/about>About</a>")

def about(request):
	response=HttpResponse()
	response.write("<p>Here's the text of the about page<p>")
	response.write("<a href=/myrango/>Index</a>")
	return response
# Create your views here.
