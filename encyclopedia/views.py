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
    content = util.get_entry(title)

    if content is not None:
        # Present user with a page that displays the content of the entry 
        return HttpResponse(f"{markdown2.markdown(content)}")
    else:
        return HttpResponse("")

def search(request):

    form = request.GET
    query = form.cleaned_data["q"]

    return render(request, "encyclopedia/search.html", {
        "entries": util.list_entries(),
        "entry": query
    })