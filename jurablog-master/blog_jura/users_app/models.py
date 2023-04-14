from django.db import models

from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your models here.


#Importo la clase Users de Django porque segun leí es mas robusta y segura que la que pueda desarrollar de manera personalizada. De esa clase, derivo como clase hijo a Author


class Author(User):
    num_followers = models.IntegerField(default=0)
    expertise = models.CharField(max_length=100, blank=True, null=True)
    academic_titles = models.CharField(max_length=100, blank=True, null=True)
    pseudonym = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.username
    
    #Enzo, esto lo hice auida de GPT, porque no sabía como hacer que el autor y el seguidor se conectaran. Es muchos a muchos, pero ¿Cómo
    #hago que no se dupliquen? Le pregunté a GPT y he aquí la rta. En honor a la honestidad intelectual, yo pensé en definir dos modelos, autor y follow y generar el puente entre ellos, pero el puente es made in GPT.

    def __str__(self):
        return self.username

    # def get_followers(self):
    #     return self.followers.all()    #Esta función quisiera pasarla a las Views, pero  no me reconoce el atributo followers (se queda en blanco, y tengo mierdo de migrar y romper todo, ya me paso 20 veces :(   )


class Best_seller_author(Author):
    best_seller_ranking = models.IntegerField()


     
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.TextField()
    tags = models.CharField(default=None, max_length=200, blank=True)
    category = models.CharField(default ="Actualidad", max_length=50, blank=True)

  # author = models.ForeignKey(Author, on_delete=models.CASCADE)  Comenté este campo porque me rompe todo cuando quiero agregar un nuevo post. 

    def __str__(self):
        return f"{self.title} - {self.author}"


# class Follow(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='followed_by')
#     followed_date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'author')

#     def __str__(self):
#       return "Seguidores"

