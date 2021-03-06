from django.shortcuts import render
from django.http import HttpResponse
#import the Category model
from myrango.models import Category
from myrango.models import Page

#def index(request):
#	context_dict={'boldmessage':"I am bold font from the context"}
#	return render(request,'myrango/index.html',context_dict)
def about(request):
	response=HttpResponse()
	response.write("<p>Here's the text of the about page<p>")
	response.write("<a href=/myrango/>Index</a>")
	return response

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
  #  category_list = Category.objects.all()[:5]
  #  context_dict = {'categories': category_list}

    page_list = Page.objects.all()
    context_dict = {'pages': page_list}
    # Render the response and send it back!
    return render(request, 'myrango/index.html', context_dict)

# Create your views here.

def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'myrango/category.html', context_dict)

def page(request, page_title_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        page = Page.objects.get(slug=page_title_slug)
        context_dict['page_title'] = page.title

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        #pages = Page.objects.filter(page=page)

        # Adds our results list to the template context under name pages.
       # context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = page.category
	context_dict['url']=page.url
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'myrango/page.html', context_dict)
