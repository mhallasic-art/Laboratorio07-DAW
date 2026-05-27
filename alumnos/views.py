from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista.html', {'alumnos': alumnos})


def crear_alumno(request):
    form = AlumnoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_alumnos')

    return render(request, 'alumnos/form.html', {'form': form})