from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Bb


def old_index(request):
    title = 'Список объявлений\n\n\n'
    full_content = ''
    for board in Bb.objects.order_by('-published'):
        full_content = full_content + board.title + '\n\n'
        full_content = full_content + board.content + '\n'
        full_content = full_content + '=' * 50 + '\n'
    return HttpResponse(title + full_content, content_type='text/plain; charset=utf-8')


def odl1_index(request):
    template = loader.get_template('index.html')
    bboards = Bb.objects.order_by('-published')
    context = {'bbs': bboards}
    return HttpResponse(template.render(context, request))


def index(request):
    bboards = Bb.objects.all()
    rendered = render(request, 'index.html', {'bbs': bboards})
    return rendered


def demo(request):
    msg = "Демонстрационная запись для модуля bboard."
    return HttpResponse(msg)
