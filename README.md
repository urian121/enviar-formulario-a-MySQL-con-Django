APRENDIENDO DJANDO PASO A PASO

1.  Crear un entorno virtual, hay muchas formas

    - Opcion 1: Crear entorno virtual con el paquete virtualenv
      Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de
      https://pypi.org/project/virtualenv/
      pip install virtualenv
      virtualenv env
      virtualenv --version
    - Opcion 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
      python -m venv env

2.  Activar ambiente virtual en Mac
    source env/bin/activate
    deactivate -->Para desactivar mi entorno virtual

3.  Instalar Djando desde el manejador de paquete de Python Pip, el entorno virtual.
    python -m pip install Django
    pip install Django
    Nota: para instalar Django en una version especifica
    pip install Django==4.2.4

4.  Instalar Driver para conectar Gestor de BD MySQL con Django
    pip install mysqlclient

5.  Crear el proyecto con Djando
    django-admin startproject project_core .
    El punto . es crucial porque le dice al script que instale Django en el directorio actual,
    para el cual el punto sirve de abreviatura

    - Ya en este punto se puede correr el proyecto que a creado Django,
      python manage.py runserver

6.  Crear el archivo requirements.txt para tener todos mis paquetes a la mano
    pip freeze > requirements.txt
    Nota: para instalar los paquetes solo basta ejecutar

    - pip install -r requirements.txt

7.  Crear mi primera aplicación en Django
    python manage.py startapp crud_libros

8.  Instalar nuestra aplicación (crud_libros) ya creada en el proyecto
    archivo settings.py
    INSTALLED_APPS = [
    ----,
    'crud_libros',
    ]

9.  Crear un Modelo en models.py de nuesta aplicacion, cada clase de nuestro modelo representa una tabla en nuestra BD (bd_crud_django) prefesiblemento los modelos
    se declaran en singular
    class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

10. crear la Base de Datos (bd_crud_django) en MySQL

11. Crear las migraciones que estan en mi modelo
    python manage.py makemigrations crud_libros

12. Correr migraciones
    python manage.py migrate

13. Creamos un usuario para entrar al CPanel de Django y poder ver mis modelos (tablas)
    python manage.py createsuperuser

14. Ya se puede acceder al CPanel de Django atraves de la URL http://127.0.0.1:8000/admin/ estando alli solo nos logueamos con
    los datos que hemos creado hace un momento. Desde aqui podemos hacer las operaciones CRUD de nuestra aplicación.

15. Para visualizar cada modelo en el CPanel de django tengo que ir al archivo admin.py de mi aplicación
    e importar el modelo y registrarlo en el CPanel admin de django

16. Configurar la conexión a la Base de Datos
    DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'crud_django',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
    }
    }

17. En el archivo views.py de mi apliación crear una vista (función)
    from django.http import HttpResponse

    def inicio(resquest):
    return HttpResponse("Hola Mundo", status=200)

18. Crear el archivo urls.py en la aplicación (crud_libros)
    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.inicio, name='inicio'),
    ]

19. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('crud_libros.urls')),
    ]

20. Revisar la consola y visitar la URL http://127.0.0.1:8000

21. Crear la carpeta 'templates' dentro de mi aplicación donde estarán mis archivos .html

22. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

COMANDO ADICIONALES:

- para verificar si tienes python instalado solo baston con ejecutar
  python --version
  tambien se verifica si tienes PIP el administrador de paquetes para Python instalado que ya desde la version 3.4 ya viene includo con python es
  decir que al instalar Python podria verificar si tiene pip asi:
  pip --version
  Si no lo tiene instalado lo puede instalar asi:
  https://pypi.org/project/pip/
  pip install pip

3. ver todo el historial de migraciones:
   python manage.py showmigrations

4. listar paquetes del instalador en el proyecto
   pip list
   pip freeze

5. Version de Djando en mi proyecto
   python -m django --version

6. Instalar Paquete para crear variables de entorno
   pip install django-environ

7. Correr archivo requirement.txt
   pip install -r requirements.txt

Jinja2 (una biblioteca de plantillas)
Django es un framework web gratuito y de código abierto publicado por primera vez en 2005 por
Adrian Holovaty y Simon Willison.

Django es un sofisticado framework basado en Python con configuraciones de desarrollo de pila completa,
como diseños de plantillas, solicitud y resolución de problemas, cookies, validación de formularios,
pruebas unitarias, configuración de tablas y otras funcionalidades que los desarrolladores
utilizan para crear aplicaciones web dinámicas.

Django sigue un patrón arquitectónico Modelo-Vista-Plantilla (MVT) que ayuda a los desarrolladores a
realizar tareas rutinarias o complejas de forma eficiente con poca intervención de protocolos,
administración y sistemas al crear aplicaciones de alta intensidad y sitios web basados en bases de datos.
Importante Djando genera las migraciones a partir de la informacion que existe en el modelo

---

Un proyecto en Django vs aplicacion (son como modulos de mi proyecto) en Django, en generar un
proyecto en Django esta compuesto por aplicaciones.

amazon.com -> es el proyecto
usuarios ->crear, editar, borrar, recuperar etc seria mi aplicacion o modulo
tienda ->agregar, producto, borrar, editar, enviar producto etc.

---

Los modelos Django proporciona una capa de abstracción
(los «modelos») para estructurar y manipular los datos de su aplicación web.

Crear administrador:
python manage.py createsuperuser
Luego escribir cualquier usuario y clave
Las migraciones comprenden;la autentiticafion por defecto de Django
Existen vistas de clases y vistas de funciones.

Las vistas en Django son funciones de Python que reciben solicitudes HTTP y devuelven una respuesta HTTP, como un documento
HTML.

Un QuerySet es una colección de datos de una base de datos.
