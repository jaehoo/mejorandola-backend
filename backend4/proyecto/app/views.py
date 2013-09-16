# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http.response import HttpResponseRedirect
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by("-votos")
    template = "index.html"
    return render(request, template,{"categorias" : categorias, "enlaces":enlaces, "request":request})


def categoria(request, id_categoria):
    # categorias = Categoria.objects.all()
    cat = Categoria.objects.get(pk = id_categoria)
    categorias=[cat]
    cat = get_object_or_404(Categoria, pk = id_categoria)
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "index.html"
    return render(request,template,locals())

def hora_actual(request):
    ahora = datetime.now()
    t = get_template('hora.html')
    c = Context({'hora': ahora, 'usuario':'jaehoo'})
    html = t.render(c)
    return HttpResponse(html)

def hora_actual2(request):
    now = datetime.now();
    return render_to_response('hora.html',{'hora': now, 'usuario':'JAEHOO'})

@login_required
def plus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos = enlace.votos +1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def minus(request, id_enlace):
    enlace = Enlace.objects.get(pk=id_enlace)
    enlace.votos = enlace.votos -1
    enlace.save()
    return HttpResponseRedirect("/")


@login_required
def add(request):
    #categorias = Categoria.objects.all()
    if request.method == "POST":
        form = EnlaceForm(request.POST)
        if form.is_valid():
            #form.save()
            enlace = form.save(commit =False)
            enlace.usuario = request.user
            enlace.save()
            return HttpResponseRedirect("/")
    else:
        form = EnlaceForm()

    template = "form.html"
    return render_to_response(template,
                              context_instance = RequestContext(request,locals()))
