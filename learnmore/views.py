from django.shortcuts import render

# Create your views here.
def learn_more(request):
    """ A view to return the learn more page"""
    return render(request, 'learnmore/learn_more.html')