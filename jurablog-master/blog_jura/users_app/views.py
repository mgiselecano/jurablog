from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *
# Create your views here.


#NAV-BAR
def home (self):
     return render (self, "home.html")

def author (self):
     return render (self, "author.html")

def blog (self):
     posts = Post.objects.all()
     return render (self, "blog.html", {"posts": posts} )


def post (self):
     return render (self, "post.html")

def new_post (self):
     return render (self, "new_post.html")

def authors (self):
     return render (self, "author.html")

def team (self):
     return render (self, "team.html")

def contact (self):
     return render (self, "contact.html")



#BLOG - POST

# def create_new_post (request):
#     print ("method: ", request.method)
#     print ("post: ", request.POST)

#     if request.method == "POST":
         
#          post = Post(author=request.POST["author"],title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], tags=request.POST["tags"])
#          post.save()

#          return render (request, "published_post.html") 

#     return render (request, "create_new_post.html")


def create_new_post (request):
    print ("method: ", request.method)
    print ("post: ", request.POST)

    if request.method == "POST":
        
        new_post_form = Form_new_post(request.POST)
          
        print(new_post_form)

        if new_post_form.is_valid():
             
          data = new_post_form.cleaned_data
   
          post = Post(author=data["author"],title=data["title"], content=data["content"], category=data["category"], tags=data["tags"])
          post.save()
        
          return render (request, "published_post.html") 
        
        else:
             return render (request, "published_post.html", {"Mensaje": "Formulario inválido"}) 
    
    else:    
        new_post_form = Form_new_post()

        return render (request, "create_new_post.html", {"new_post_form": new_post_form})
    

def search_post(request):
    
    return render (request, "search_post.html")

def found_post(request):
    if request.GET["title"]:
        title = request.GET["title"]
        posteos = Post.objects.filter(title__icontains=title)
        return render(request, "found_post.html", {"title": title, "posteos": posteos})
    else:
        
      return HttpResponse(f'No enviaste info')
#     if request.method == "GET":
#         title = request.POST.get("title")
#         print (title)
#         if title:
#             post = Post.objects.filter(title__icontains=title)
#             return render(request, "found_post.html", {"title": title, "post": post})
#         else:
#             return render(request, "found_post.html", {"error": "Por favor, ingrese un título válido."})
#     else:
#         return render(request, "found_post.html")

# Redacción del profe que me corrigió CoderAsk porque me dijeron que tiene que se tipo POST, no GET

# def found_post(request):
#     if request.GET ["title"]:
#         title = request.GET ["title"]
#         matching_post = Post.objects.filter(title=title)
#         return render(request, "found_post.html", {"matching_post": matching_post})
#     else:
#         return HttpResponse("No tenemos articulos con ese titulo info")


# Redacción mía despues de mil iteraciones en base a CoderAsk y GPT
    


# def found_post(request):
#     # print ("method: ", request.method)
#     # print ("post: ", request.POST)
#     title = request.POST.get("title")    #si pongo title entre cocrchetes como hace el profe me da error TypeError: 'method' object is not subscriptable
#     if request.POST.get("title"):
#         matching_post = Post.objects.filter(title=title)
#         print(matching_post)
#         return render(request, "found_post.html", {"matching_post": matching_post})
#     else:
#         return HttpResponse("No tenemos articulos con ese titulo info")


# def found_post(request):
#     title = request.POST.get("title")
#     if title:
#         matching_post = Post.objects.filter(title__icontains=title)
#         if matching_post:
#             return render(request, "found_post.html", {"matching_post": matching_post})
#         else:
#             return HttpResponse("No se encontraron artículos con ese título")
#     else:
#         return HttpResponse("Ingrese un título para buscar")

#Prueba coderask



def post_new_post (request):
    print ("method: ", request.method)
    print ("post: ", request.POST)
    return render (request, "published_post.html")



def published_post (request):
  return render (request, "published_post.html")

def delete_post (request, id):
     
     if request.method =="POST":
          
          post = Post.objects.get(id=id)   #el ID de la izq es el de la BD
          post.delete ()    

          post = Post.objects.all()
          return render (request, "delete_post.html", {"post": post})
     




#AUTORES

def author_list (self):
     return render (self, "author.html")

def get_publications(self):          #Función para listar todos los post realizados por una persona.
      post_list = Post.objects.all()  #Los managers son los que nos entregasn la URL de Django y conecta con la BD. Es el nexo con la BD
     
      return render (self, "post_list.html", {"post_list": post_list}) 

def get_authors (request):
     authors = Author.objects.all()
     return render (request, "get_authors.html")

def new_author (self, user_name, badges, expertise, academic_titles,):
    author = Author (user_name=user_name, badges=0, expertise=expertise, academic_titles=academic_titles)
    author.save()

    return HttpResponse (f"""
      <p> Tu perfil {author.user_name} se creó correctamente. ¡Te damos la bienvenida!<p>
      """)


def create_new_author (request):
    print ("method: ", request.method)
    print ("post: ", request.POST)

    if request.method == "POST":
        
        new_author_form = Form_new_author(request.POST)
          
       
        if new_author_form.is_valid():
             
          data = new_author_form.cleaned_data
   
          post = Post(first_name=data["first_name"],last_name=data["last_name"], email=data["email"], user_name=data["user_name"])
          post.save()
          return render (request, "create_new_author.html") 
        
        else:
             return render (request, "create_new_author.html", {"Mensaje": "Formulario inválido"}) 
    
    else:    
        new_author_form = Form_new_post()

        return render (request, "create_new_author.html", {"new_author_form": new_author_form})


def search_author(request):
    
    return render (request, "search_author.html")



def found_author(request):
    if request.GET["pseudonym"]:
        autor = request.GET["pseudonym"]
        autores = Author.objects.filter(pseudonym__icontains=autor)
        print(autores)
        return render(request, "found_author.html", {"autor": autor, "autores": autores})
    else:
        
      return HttpResponse(f'No enviaste info')
#     pseudonym = request.POST.get("pseudonym")
#     print ("method: ", request.method)
#     print ("post: ", request.POST)
#     if pseudonym:
#         matching_authors = Author.objects.filter(pseudonym=pseudonym)
#         return render(request, "found_author.html", {"pseudonym": pseudonym, "matching_authors": matching_authors})
#     else:
#         return HttpResponse("No enviaste info")