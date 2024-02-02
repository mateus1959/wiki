from django.shortcuts import render
from django.http import HttpResponse
from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Displays the contents of the encyclopedia entry 
def entry(request, title):

    # Get the content of the encyclopedia entry -> util.get_entry(title)
    # Convert markdown content to HTML -> markdown2.markdown(util.get_entry(title))
    # Present user with a page that displays the content of the entry 
    return HttpResponse(f"{markdown2.markdown(util.get_entry(title))}")

