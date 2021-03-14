from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def catch_all(request, url):
    return redirect ("/")

def result(request):
   #Good Practice
   request.session['name'] = request.POST['name']
   request.session['location'] = request.POST['location']
   request.session['language'] = request.POST['language']
   request.session['description'] = request.POST['description']
   request.session['counter'] = 100
   return redirect('/thanks')

def thanks(request):
    print(request.session)
    
    return render(request, "result.html")

