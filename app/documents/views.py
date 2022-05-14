from django.shortcuts import render
from django.views.generic import TemplateView

from core import InitializeBooleanModel
from core.basics import Consult


class HomePageView(TemplateView):
    template_name = 'home.html'


def SearchResultsView(request):
    template_name = 'search_results.html'
    q = request.GET.get("q")
    model = request.GET.get("model")
    data = {}
    print("Query = ", q, " Model = ", model)

    query = Consult(id=1, content=q)

    if model == "Boolean":
        boolean = InitializeBooleanModel()
        docs = boolean.Consult(query)
        data = {
            "docs": docs
        }

    return render(request, template_name, data)
