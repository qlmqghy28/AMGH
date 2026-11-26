from django.shortcuts import render

def inicio (request):
     return render (request, 'GONZALEZ/inicio.html')
def registro(request):
    if request.method == 'POST':
         nombre = request.POST.get('name')
         apellidop = request.POST.get('apellidop')
         apellidom = request.POST.get('apellidom')
         edad = request.POST.get('edad')
         genero = request.POST.get('genero')
         intereses = request.POST.getlist('intereses')

         print('Tus datos registrados son: ')
         print('Nombre: ',nombre)
         print('Apellido Paterno: ', apellidop)
         print('Apellido Materno: ', apellidom)
         print('Edad: ', edad)
         print('Genero: ', genero)
         print('Interes: ', intereses )
         
    return render(request,  'GONZALEZ/formregistro.html')
def encuesta(request):
     return render(request, 'GONZALEZ/formencuesta.html')