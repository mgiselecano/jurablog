from django.contrib import admin
from django.urls import path
from users_app.views import *


urlpatterns = [

  # NAVBAR
  path ("home", home, name="Inicio"),
  path ("blog/", blog, name="Articulos"),
  path ("post/", post, name="Leer mas"),
  path ("team/", team, name="Nosotros"),
  path ("contact/", team, name="Contacto"),
 
  # BLOG - POST

  path("create_new_post/", create_new_post, name="Nuevo_post"),
  path("post_new_post/", post_new_post, name="Publicar"),
  path( "search_post", search_post, name="Buscar_post"),
  path( "found_post", found_post, name="Resultado_post"),



  #AUTORES
  path ("autor/", author, name="Autores"),
  path("create_new_author/", create_new_author, name="Nuevo_autor"),
  path ("published_post/", author_list, name="Lista_de_autores"),
  path ("author_list/", author_list, name="Lista_de_autores"),
  path ("signup/", new_author),
  path ("publicacionesporautor/", get_publications),
  path( "search_author", search_author, name="Buscar_autor"),
  path( "found_author", found_author, name="Resultado_autor"),

]


