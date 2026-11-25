from django.shortcuts import render

def inicio (request):
     return render (request, 'GONZALEZ/inicio.html')
def registro(request):
    return render(request,  'GONZALEZ/formregistro.html')
def encuesta(request):
     return render(request, 'GONZALEZ/formencuesta.html')