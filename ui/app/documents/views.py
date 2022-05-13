from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def SearchResultsView(request):
    query = request.GET.get("q")
    print("Query = ", query)
    model = {
        "docs": [
            {
                "name": "T1",
                "author": "A1"
            },
            {
                "name": "T2",
                "author": "A2"
            }
        ]
    }

    template_name = 'search_results.html'
    return render(request, template_name, model)
