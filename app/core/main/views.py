from django.shortcuts import render

# Create your views here.
def index(request):    
    docs = [
        {
            "title":"Title",
            "author" : 'Author',    
        },
        {
            "title":"Title",
            "author" : 'Author',    
        }
    ]

    data = {
        "title" : "Documents",
        "documents" : docs, 
    }

    return render(request,'index.html',data)