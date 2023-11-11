from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import markdown2

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'id': 'npf-title-input', 'class': 'form-control', 'name': 'title'}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'id': 'npf-description-area', 'class': 'form-control', 'name': 'description'}), required=False)
    button = forms.CharField(label="", widget=forms.TextInput(attrs={'id': 'npf-button', 'class': 'btn btn-primary', 'type': 'submit', 'value': 'Create Page'}))



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
    query = query.strip() if query != None else ''

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


def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            dsc = form.cleaned_data["description"]
            
            if util.get_entry(title):
                form.add_error('title', 'This page already exists')
                return render(request, "encyclopedia/new_page.html", {
                    "form": form
                })

            util.save_entry(title, dsc)
            return HttpResponseRedirect(reverse("entries", kwargs={'name': title}))
        else: 
            return render(request, "encyclopedia/new_page.html", {
                "form": form
            })
    
    return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm()
    })