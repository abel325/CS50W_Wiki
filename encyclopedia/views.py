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