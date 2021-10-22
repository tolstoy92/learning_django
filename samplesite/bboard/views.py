from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView

from .models import Bb, Rubric
from .forms import BbForm


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
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bboards,
        'rubrics': rubrics
    }
    rendered = render(request, 'index.html', context)
    return rendered


def demo(request):
    msg = "Демонстрационная запись для модуля bboard."
    return HttpResponse(msg)


def by_rubric(request, rubric_id):
    bboards = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bboards,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'add.html'
    form_class = BbForm
    success_url = '/bboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
