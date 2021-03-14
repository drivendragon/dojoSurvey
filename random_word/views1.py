rom django.http import HttpResponse, Http404
from django.shortcuts import render
import string
import random


# Create your views here.

def index(request):
  try:
    request.session['counter'] += 1
  except:
    request.session['counter'] = 1



  print request.session['counter']


  word = ''.join(random.choice(string.lowercase) for i in range(14))

  context = {
    "word" : word
  }



  return render(request, 'rand_word/index.html', context)
