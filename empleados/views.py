from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Empleado



# Create your views here.


def inicio(request):
    return render(request, 'form_empleado.html')


def process_form(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        precio = request.POST.get('precio')

        nuevo_libro = Empleado(titulo=titulo, autor=autor, precio=precio)
        nuevo_libro.save()

        messages.success(
            request, "Felicitaciones, el libro fue registrado correctamente")

        return redirect('list_libros')

    # Renderiza el formulario en caso de método GET
    return render(request, 'formulario_libro.html')
