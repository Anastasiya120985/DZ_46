from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from django.utils.translation import ugettext as _

cars = {'toyota': 'Тойота', 'honda': 'Хонда', 'renault': 'Рено'}
headphone_models = {'budslive': 'Samsung Galaxy Buds Live', 'airpods': 'Apple AirPods'}
languages = {'fr': 'Французский', 'de': 'Немецкий', 'es': 'Английский'}
week_days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
date_now = datetime.datetime.now()


def index(request):
    # output = _('StatusMsg')
    template = loader.get_template("index.html")
    context = {'title': 'DZ_46',
               'cars': cars.items(),
               'headphone_models': headphone_models.items(),
               'languages': languages.items(),
               'day': week_days[date_now.weekday()],
               }
    return HttpResponse(template.render(context, request))


def info_cars(request, car):
    template = loader.get_template("info.html")
    context = {'title': 'DZ_46',
               'text': cars[car],
               'cars': cars.items(),
               'headphone_models': headphone_models.items(),
               'languages': languages.items(),
               'day': week_days[date_now.weekday()]
               }
    return HttpResponse(template.render(context, request))


def headphones(request):
    if request.GET:
        model = request.GET.get('model')
        template = loader.get_template("info.html")
        context = {'title': 'DZ_46',
                   'text': headphone_models[model],
                   'cars': cars.items(),
                   'headphone_models': headphone_models.items(),
                   'languages': languages.items(),
                   'day': week_days[date_now.weekday()]
                   }
        return HttpResponse(template.render(context, request))


