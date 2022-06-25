from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django import forms
from django.forms import formset_factory

from core.boolean.BooleanModel import BooleanModel
from core.vectorial.VectorialModel import VectorialModel
from core.probabilistic.ProbabilisticModel import ProbabilisticModel

from core.fileProcessing.Loader import *
from core.basics import Consult
from core.basics.BasicModel import BasicModel
from time import time

cranUrl = "./Test Collections/Cran/"
imdbUrl = "./Test Collections/imdb/"
newsgroupUrl = "./Test Collections/Newsgroups/"

class ModelWrapper:
    def __init__(self):
        self.model = None
        self.modelname = None
        self.dataset = None
    def GetModel(self, modelname, dataset):
        if self.modelname == modelname and self.dataset == dataset:
            return self.model
        self.modelname = modelname
        self.dataset = dataset
        if dataset == "cran": documents, _ = LoadCranDataset(cranUrl)
        elif dataset == "imdb": documents = LoadIMDBDataset(imdbUrl)
        else: documents = LoadNewsgroupDataset(newsgroupUrl)

        if modelname == "Boolean": self.model = BooleanModel(documents)
        elif modelname == "Vectorial": self.model = VectorialModel(documents)
        elif modelname == "Probabilistic": self.model = ProbabilisticModel(documents)
        return self.model

wrapper = ModelWrapper()

class RetroalimentationForm(forms.Form):
    checkbox = forms.BooleanField(required=False)
    id = forms.CharField(widget=forms.HiddenInput)
    # text = forms.CharField(widget=forms.HiddenInput)

class HomePageView(TemplateView):
    template_name = 'home.html'

def RedirectView(request):
    modelname = request.POST.get('model')
    dataset = request.POST.get('dataset')
    return redirect('model', modelname=modelname, dataset=dataset)


def ModelView(request, modelname, dataset):
    template_name = 'search_results.html'

    model = wrapper.GetModel(modelname, dataset)

    size = request.GET.get("size")
    size = 20 if size is None else int(size)
    q = request.GET.get("q")
    data = {"relaxed": False, "iterations": 1, "retroalimentation": False}
    q = "" if q is None else q
    print("Query = ", q, " Model = ", modelname)
    docs = []
    query = Consult(id=1, content=q)
    begTime = time()
    if modelname == "Boolean":
        relaxedConsult = request.GET.get('relaxed')
        data['relaxed'] = relaxedConsult == 'on'
        if not q == "":
            docs = model.Consult(query, size=size, relaxed=(relaxedConsult == 'on'))
    elif modelname == "Vectorial":
        retroalimentation = request.GET.get('retroalimentation')
        data['retroalimentation'] = retroalimentation == 'on'

        if not q == "":
            if retroalimentation == 'on' and request.method == "POST":
                relevant, irrelevant = [], []
                for item in request.POST.getlist('retro'):
                    x, y = item.split()
                    if y == 'irrelevant': irrelevant.append(int(x))
                    else: relevant.append(int(x))
                print(relevant, irrelevant)
                docs = model.ReConsult(query, size=size, relevant=relevant, irrelevant=irrelevant)
            else:
                docs = model.Consult(query, size=size)
    else:
        iterations = request.GET.get('iterations')
        iterations = 1 if iterations is None else int(iterations)
        data['iterations'] = iterations
        if not q == "":
            docs = model.Consult(query, size=size, retroalimentation=iterations)

    data["docs"] = docs
    data["model"] = modelname
    data['dataset'] = dataset
    data["q"] = q
    data["size"] = size
    data["time"] = round(time() - begTime, ndigits=2)

    return render(request, template_name, data)
