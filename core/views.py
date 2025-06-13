from django.shortcuts import render

# Vista para la página principal (Inicio)
def home(request):
    return render(request, 'home.html')

# Vista para la página "Acerca de mí"
def about(request):
    return render(request, 'about.html')

