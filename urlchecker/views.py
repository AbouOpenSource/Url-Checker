from django.http import HttpResponse
from django.shortcuts import render
import joblib
from . import utils
import numpy as np


def home(request):
    return render(request, "urlchecker/home.html",{})

def resutl(request):
    model = joblib.load("finalized_model.sav")
    data = utils.pre_processing_of_query(request.GET['query'])
    answer = model.predict([data])
    print(answer)
    if answer == 0:
        return render(request, "urlchecker/positive.html",{"answer": answer,"query" : request.GET['query'] })
    else:
        return render(request, "urlchecker/negative.html",{"answer": answer,"query" : request.GET['query'] })
