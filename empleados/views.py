from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Empleado


# Create your views here.


def inicio(request):
    opciones_edad = [(str(edad), str(edad)) for edad in range(18, 51)]
    contexto = {
        'opciones_edad': opciones_edad,
    }
    return render(request, 'form_empleado.html', contexto)


def registrar_empleado(request):
    context = {}  # Inicializa un diccionario de contexto
    if request.method == 'POST':
        nombre = request.POST.get('nombre_empleado')
        apellido = request.POST.get('apellido_empleado')
        email = request.POST.get('email_empleado')
        edad = request.POST.get('edad_empleado')
        genero = request.POST.get('genero_empleado')
        salario = request.POST.get('salario_empleado')

        # Procesa los datos y guarda en la base de datos (ejemplo)
        empleado = Empleado(
            nombre_empleado=nombre,
            apellido_empleado=apellido,
            email_empleado=email,
            edad_empleado=edad,
            genero_empleado=genero,
            salario_empleado=salario,
        )
        empleado.save()

        # Redirige al usuario a otra página (puede ser una página de éxito)
        # Reemplaza 'pagina_exito' con la URL deseada
        return redirect('inicio')

    # Si no se ha enviado el formulario, simplemente renderiza la plantilla con el formulario vacío
    return render(request, 'formulario_libro.html', context)


def listar_empleados(request):
    empleados = Empleado.objects.all()  # Obtiene todos los registros de empleados

    contexto = {
        'empleados': empleados,
    }

    return render(request, 'lista_empleados.html', contexto)
