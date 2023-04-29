from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse


def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data is inserted')
        else:
            return HttpResponse('data is not inserted')


    return render(request,'insert_topic.html',d)


def insert_web(request):
    WO=WebpageForm()
    d={'WO':WO}
    if request.method=='POST':
        WOD=WebpageForm(request.POST)
        if WOD.is_valid():
            WOD.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data is not inserted')
    return render(request,'insert_web.html',d)