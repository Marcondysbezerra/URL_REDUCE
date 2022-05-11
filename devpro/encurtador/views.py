from devpro.encurtador.models import UrlRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse


def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destino)