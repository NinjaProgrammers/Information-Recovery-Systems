from django.shortcuts import render
from django.views.generic import TemplateView
from django import forms
from django.forms import formset_factory

from core.InitializeBooleanModel import InitializeBooleanModel
from core.InitializeVectorialModel import InitializeVectorialModel
from core.InitializeProbabilisticModel import InitializeProbabilisticModel
from core.basics import Consult
from time import time

boolean = InitializeBooleanModel()
vectorial = InitializeVectorialModel()
probabilistic = InitializeProbabilisticModel()

class RetroalimentationForm(forms.Form):
    checkbox = forms.BooleanField(required=False)
    id = forms.CharField(widget=forms.HiddenInput)
    # text = forms.CharField(widget=forms.HiddenInput)

class HomePageView(TemplateView):
    template_name = 'home.html'


def ModelView(request, model):
    template_name = 'search_results.html'

    size = request.GET.get("size")
    size = 20 if size is None else int(size)
    q = request.GET.get("q")
    q = "" if q is None else q
    print("Query = ", q, " Model = ", model)

    data = {"relaxed": False, "iterations": 1, "retroalimentation": False}
    query = Consult(id=1, content=q)
    begTime = time()
    if model == "Boolean":
        relaxedConsult = request.GET.get('relaxed')
        data['relaxed'] = relaxedConsult == 'on'
        docs = boolean.Consult(query, size=size, relaxed=(relaxedConsult == 'on'))
    elif model == "Vectorial":
        retroalimentation = request.GET.get('retroalimentation')
        data['retroalimentation'] = retroalimentation == 'on'

        if retroalimentation == 'on' and request.method == "POST":
            relevant, irrelevant = [], []
            for item in request.POST.getlist('retro'):
                x, y = item.split()
                if y == 'irrelevant': irrelevant.append(int(x))
                else: relevant.append(int(x))
            print(relevant, irrelevant)
            docs = vectorial.ReConsult(query, size=size, relevant=relevant, irrelevant=irrelevant)
        else:
            docs = vectorial.Consult(query, size=size)
    else:
        iterations = request.GET.get('iterations')
        iterations = 1 if iterations is None else int(iterations)
        data['iterations'] = iterations
        docs = probabilistic.Consult(query, size=size, retroalimentation=iterations)

    data["docs"] = docs
    data["model"] = model
    data["q"] = q
    data["size"] = size
    data["time"] = round(time() - begTime, ndigits=2)

    return render(request, template_name, data)
