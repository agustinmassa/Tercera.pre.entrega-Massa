
from django.shortcuts import render
from App1.models import Curso, Profesor, Estudiante
from django.http import HttpResponse
from App1.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario 


# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def cursos(request):
    return render(request,'App1/cursos.html')
def profesores(request):
    return render(request,'App1/profesores.html')
def estudiantes(request):
    return render(request,'App1/estudiantes.html')


def cursos(request):
    if request.method =='POST':
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'App1/cursos.html', {"miFormulario": miFormulario})

def profesores(request):
    if request.method =='POST':
        miFormulario=ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Profesor(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['profesion'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario=ProfesorFormulario()
    return render(request, 'App1/profesores.html', {"miFormulario": miFormulario})

def estudiantes(request):
    if request.method =='POST':
        miFormulario=EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Estudiante(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario=EstudianteFormulario()
    return render(request, 'App1/estudiantes.html', {"miFormulario": miFormulario})



def busquedaCurso(request):
     return render(request,'App1/busquedaCurso.html')

def buscar(request):
     if request.GET['curso']:
          curso = request.GET['curso']
          cursos= Curso.objects.filter(curso__icontains=curso)

          return render(request,'App1/inicio.html', {"cursos":cursos, "comisiones": curso })
     else:
          respuesta= "No enviaste datos"

     #return HttpResponse(respuesta)
     return render(request,"App1/inicio.html",{"respuesta":respuesta})
