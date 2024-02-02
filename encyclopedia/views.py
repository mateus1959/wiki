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

    # Get the content of the encyclopedia entry 
    entry = util.get_entry(title)

    # Convert markdown content to HTML 
    html = markdown2.markdown(entry)

    # Present user with a page that displays the content of the entry 
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "html": html
    })

