from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import markdown2
from django.core.files.storage import default_storage
from random import choice

from . import util


class PageForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'id': 'pf-title-input', 'name': 'title'}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'id': 'pf-description-area', 'name': 'description'}), required=False)


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
            "entry": htmlEntry,
        })
    else:
        return render(request, "encyclopedia/entries.html", {
            "title": "Error 404",
            "entry": "<h1 style='text-align: center; font-size: 46px'> Error 404: file not found </h1>",
            "hidden": "hidden",
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
        form = PageForm(request.POST)

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
        "form": PageForm()
    })


def edit_page(request):
    if request.method == "POST":
        form = PageForm(request.POST)     
        old_title = request.POST.get('old-title') 

        if form.is_valid():
            title = form.cleaned_data["title"]
            dsc = form.cleaned_data["description"]

            if util.get_entry(title) and title != old_title:
                form.add_error('title', 'A page with this name already exists')
                return render(request, "encyclopedia/edit_page.html", {
                    "form": form,
                    "old_title": old_title
                })
            
            filename = f"entries/{old_title}.md"
            if default_storage.exists(filename):
                default_storage.delete(filename)
            else:
                return HttpResponseRedirect(reverse('index'))
            util.save_entry(title, dsc)
            return HttpResponseRedirect(reverse("entries", kwargs={"name": title}))
        else:
            return render(request, "encyclopedia/edit_page.html", {
                "form": form,
                "old_title": old_title
            })

    title = request.GET.get('title')
    dsc = util.get_entry(title)
    form = PageForm(initial={'title': title, 'description': dsc})

    return render(request, "encyclopedia/edit_page.html", {
        "form": form,
        "old_title": title
    })


def random_page(request):
    entries = util.list_entries()
    randp = choice(entries)
    return HttpResponseRedirect(reverse('entries', kwargs={'name': randp}))


def delete_page(request, title):
    if request.method == 'GET':
        # title = request.POST.get('title')
        util.delete_entry(title)
        return HttpResponseRedirect(reverse('index'))
    # return HttpResponseRedirect(reverse('confirm_delete', kwargs={"title": title}))

def confirm_delete(request, title):
    if request.method == 'POST':
        # title = request.POST.get('title')
        return HttpResponseRedirect(reverse('delete_page', kwargs={'title': title}))
    
    title = request.GET.get('title')
    return render(request, "encyclopedia/confirm_delete.html", {"title": title})