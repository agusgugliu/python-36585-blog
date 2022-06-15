from django.db import models

# Create your models here.

class ModelBlog(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Título ➜ {self.titulo}\nSub-Título ➜ {self.subtitulo}\nCuerpo ➜ {self.cuerpo}\nAutor ➜ {self.autor}\nFecha ➜ {self.fecha}'