from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entries(request, name):
    entry = util.get_entry(name)
    if entry != None:
        htmlEntry = markdown2.markdown(entry)
        return render(request, "encyclopedia/entries.html", {
            "title": name,
            "entry": htmlEntry
        })
    else:
        return render(request, "encyclopedia/entries.html", {
            "title": "Error 404",
            "entry": "<h1 style='text-align: center;'> Error 404: file not found </h1>"
        })
    

def search(request):
    query = request.GET.get('q')
    if query and not util.get_entry(query):
        return HttpResponseRedirect(reverse('search_results', kwargs={'query': query}))
    elif not query:
        return HttpResponseRedirect(reverse('index'))
    
    return HttpResponseRedirect(reverse('entries', kwargs={'name': query}))


def search_results(request, query):
    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "entries": util.list_entries(),
    })
