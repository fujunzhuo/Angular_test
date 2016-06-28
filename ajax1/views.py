# coding:utf-8
from json import dumps as j
from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return render(request, 'index.html')


def json(request):
    return render(request, 'json.js')


def get1(request):
    data = {
        'post': 'name1',
        'data': 'name2'
    }
    data = j(data)
    callback = request.GET['callback']
    #print data
    print request.GET
    return HttpResponse( '%s(%s)' % (callback,data))
