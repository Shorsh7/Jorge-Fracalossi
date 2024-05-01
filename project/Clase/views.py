from django.shortcuts import render, redirect

from . import models

from .forms import ComisionForm, EstudianteForm


def home(request):
    query = models.Comision.objects.all()
    context = {"comisiones": query}
    return render(request, "Comision/index.html", context)

def create(request):
    if(request.method == "POST"):
        form = ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:comision_create")
        else:
            form2 = ComisionForm()
            return render(request, "Comision/create.html", {"error": form.errors, "form": form2})
    else:
        form = ComisionForm()
        return render(request, "Comision/create.html", {"form": form})
    
def estudiante_home(request):
    query = models.Estudiante.objects.all()
    context = {"estudiantes": query}
    return render(request, "Estudiante/index.html", context)
    
def estudiante_create(request):
    if(request.method == "POST"):
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Clase:estudiante_home")
        else:
            form2 = EstudianteForm()
            return render(request, "Estudiante/create.html", {"error": form.errors, "form": form2})
    else:
        form = EstudianteForm()
        return render(request, "Estudiante/create.html", {"form": form})
