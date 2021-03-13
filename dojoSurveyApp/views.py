from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def result(request):
    context = {
        "name": request.POST["name"],
        "location": request.POST["location"],
        "language" : request.POST["language"],
        "description" : request.POST["description"]
    }
    
    return render(request, "result.html", context)
