# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.template import RequestContext
from manageme.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from manageme.forms import *
from manageme.models import *
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('http://52.29.42.195/Project/auftraege/')
    return render_to_response('login.html', context_instance=RequestContext(request))

@login_required(login_url='/Project/login/')
def download(request, pk=None):
  fname = unicode(Auftrag.objects.get(pk=pk).aupload)
  path = os.path.join("/opt/bitnami/apps/django/django_projects/Project/media/", fname)


  #path = "C:/Users/Ulrike/PycharmProjects/Semesterprojekt/media/docs"

  with open(path, "rb") as f:
    data = f.read()
  return HttpResponse(data, content_type='application/pdf')


    #auftrage = Auftrag.objects.all().order_by('aid')

    # path = "C:\Users\Ulrike\PycharmProjects\Semesterprojekt\media\docs"
    # fname = unicode(Auftrag.objects.get(pk="001").aupload)
    #
    # with open(path, 'r') as pdf:
    #     response = HttpResponse(pdf.read(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline;filename="fname"'
    #     return response

@login_required(login_url='/Project/login/')
def get_auftraege(request):
    auftraege = Auftrag.objects.all().order_by('aid')

    return render(request, 'auftraege.html',{'page_title':'Aufträge','auftraege':auftraege})


@login_required(login_url='/Project/login/')
def neuerKunde(request):
    kunde = Kunde()

    if request.method=='POST':
        #Formular abgeschickt
        form = KundeForm(request.POST, instance=kunde)
        if form.is_valid():
            form.save()
            messages.success(request, u'Kunde gespeichert.')
            return HttpResponseRedirect(reverse('auftraege'))
        else:
            messages.error(request, u'Data incorrect')
            pass
    else:
        form = KundeForm(instance=kunde)

    return render(request,'kunde.html', {'page_title':'Neuer Kunde', 'form': form})

@login_required(login_url='/Project/login/')
def neueDienstleistung(request):
    dienstleistung = Dienstleistungsart()

    if request.method=='POST':
        #Formular abgeschickt
        form = ServiceForm(request.POST, instance=dienstleistung)
        if form.is_valid():
            form.save()
            messages.success(request, u'Dienstleistungsart gespeichert.')
            return HttpResponseRedirect(reverse('auftraege'))
        else:
            messages.error(request, u'Data incorrect')
            pass
    else:
        form = ServiceForm(instance=dienstleistung)

    return render(request,'service.html', {'page_title':'Neue Dienstleistung', 'form': form})

@login_required(login_url='/Project/login/')
def neueRechnung(request):
    rechnung = Rechnung()

    if request.method=='POST':
        #Formular abgeschickt
        form = RechnungForm(request.POST, request.FILES, instance=rechnung)
        if form.is_valid():
            form.save()
            messages.success(request, u'Rechnung gespeichert.')
            return HttpResponseRedirect(reverse('auftraege'))
        else:
            messages.error(request, u'Data incorrect')
            pass
    else:
        form = RechnungForm(instance=rechnung)

    return render(request,'rechnung.html', {'page_title':'Neue Rechnung', 'form': form})

@login_required(login_url='/Project/login/')
def auftragsdetails(request, pk=None): # wenn Primärschlüssel übergeben wird editieren, wenn nicht, neues Buch
    if pk==None:
        auftrag = Auftrag()
        page_title = 'Neuer Auftrag'
    else:
        auftrag = get_object_or_404(Auftrag, pk=pk)
        page_title = 'Auftrag bearbeiten'

    if request.method=='POST':
        form = AuftragForm(request.POST, request.FILES, instance=auftrag)
        if form.is_valid():
            form.save()
            messages.success(request,'Gespeichert')
            return HttpResponseRedirect(reverse('auftraege'))
        else:
            messages.error(request, 'Bitte Fehler korrigieren.')
    else:
        form = AuftragForm(instance=auftrag)
        return render(request, 'auftrag.html', {'page_title':page_title, 'form':form})

@login_required(login_url='/Project/login/')
def deleteAuftrag(request, pk=None):
        auftrag = get_object_or_404(Auftrag, pk=pk)
        auftrag.delete()
        #messages.success(request,'Gespeichert')
        return HttpResponseRedirect(reverse('auftraege'))




