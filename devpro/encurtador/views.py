from devpro.encurtador.models import UrlRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse


def relatorios(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = requisicao.build_absolute_uri(f'/{slug}')
    context = {
        'reduce': url_redirect,
        'url_reduzida': url_reduzida,
    }
    return render(requisicao, 'encurtador/relatorio.html', context)


def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destino)