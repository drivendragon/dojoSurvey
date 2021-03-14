from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 
get_random_string(length=14)

cat = "kitty"
randomWordGenerated = get_random_string(length=14)
print(randomWordGenerated)

def index(request):
    return render(request, "index.html")

def catch_all(request, url):
    return redirect ("/")

def result(request):
   #Good Practice
   request.session['cat'] = request.POST['cat']
   request.session['randomWordGenerated'] = request.POST['randomWordGenerated']
   request.session['counter'] = 100
   return redirect('/thanks')

def thanks(request):
    print(request.session)
    
    #return render(request, "result.html")
    return render(request, "index.html")