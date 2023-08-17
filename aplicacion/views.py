from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso
from .forms import CursoForm

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

def cursos(request):
    contexto = {'cursos': Curso.objects.all(), 'titulo': 'Cursos Disponibles -', 'comisiones': ['55630', '55640'] }
    return render(request, 'aplicacion/cursos.html', contexto)

def profesores(request):
    return render(request, 'aplicacion/profesores.html')

def estudiantes(request):
    return render(request, 'aplicacion/estudiantes.html')

def entregables(request):
    return render(request, 'aplicacion/entregables.html')

def cursoForm(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST['nombre'],
                      comision=request.POST['comision'])
        curso.save()
        return HttpResponse("Se grabo con exito el curso!")
    
    return render(request, 'aplicacion/cursoForm.html')

def cursoForm2(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get('nombre')
            curso_comision = miForm.cleaned_data.get('comision')
            curso = Curso(nombre=curso_nombre,
                          comision=curso_comision)
            curso.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = CursoForm()

    return render(request, 'aplicacion/cursoForm2.html', {"form": miForm})

def buscarComision(request):
    return render(request, 'aplicacion/buscarComision.html')

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {'cursos': cursos, 'titulo': f'Cursos que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/cursos.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')