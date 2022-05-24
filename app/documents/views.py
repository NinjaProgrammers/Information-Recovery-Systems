from django.shortcuts import render
from django.views.generic import TemplateView

from core.InitializeBooleanModel import InitializeBooleanModel
from core.InitializeVectorialModel import InitializeVectorialModel
from core.InitializeProbabilisticModel import InitializeProbabilisticModel
from core.basics import Consult

boolean = InitializeBooleanModel()
vectorial = InitializeVectorialModel()
probabilistic = InitializeProbabilisticModel()

class HomePageView(TemplateView):
    template_name = 'home.html'


def SearchResultsView(request):
    template_name = 'search_results.html'
    q = request.GET.get("q")
    model = request.GET.get("model")

    print("Query = ", q, " Model = ", model)

    query = Consult(id=1, content=q)

    if model == "Boolean":
        docs = boolean.Consult(query)
        data = {"docs": docs}
    elif model == "Vectorial":
        docs = vectorial.Consult(query, 20)
        data = {"docs": docs}
    else:
        docs = probabilistic.Consult(query, size=20, retroalimentation=True)
        data = {"docs": docs}

    return render(request, template_name, data)
