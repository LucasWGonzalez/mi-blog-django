from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Modelo principal de la app: una página o entrada de blog
class Page(models.Model):
    title = models.CharField(max_length=200)  # Campo para el título
    subtitle = models.CharField(max_length=200)  # Campo para el subtítulo
    content = RichTextField()
    image = models.ImageField(upload_to='pages_images/', blank=True, null=True)  # Imagen opcional
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que creó la página

    # Muestra el título cuando se imprime un objeto de este modelo
    def __str__(self):
        return self.title
