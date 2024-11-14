from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("index.html")
    context = dict()
    return HttpResponse(template.render(context, request))


def langs(request, lang):
    template = loader.get_template("lang.html")
    context = {'fr': {'str_1': '"Nous sommes les champions, mes amis',
                      'str_2': 'Et nous continuerons à nous battre jusqu\'à la fin"',
                      'str_3': 'Reine, nous sommes les champions'},
               'de': {'str_1': '"Wir sind die Champions, meine Freunde',
                      'str_2': 'Und wir werden bis zum Ende weiterkämpfen."',
                      'str_3': 'Königin, Wir sind die Champions'},
               'es': {'str_1': '"Somos los campeones, amigos míos',
                      'str_2': 'And we\'ll keep on fighting till the end"',
                      'str_3': 'Reina, somos los campeones'}}
    return HttpResponse(template.render(context[lang], request))
