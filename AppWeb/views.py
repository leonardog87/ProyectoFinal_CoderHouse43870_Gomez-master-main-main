from django.shortcuts import render
from .models import Blog, Mensaje, MensajeUser
from .forms import BlogForm, MensajeForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models

def inicio(request):
    return render(request,'AppWeb/inicio.html')

def aboutme(request):
    return render(request,'AppWeb/aboutMe.html')

def Paisaje(request):
    return render(request,'AppWeb/Paisaje.html')

def Publicitaria(request):
    return render(request,'AppWeb/Publicitaria.html')

def Blancoynegro(request):
    return render(request,'AppWeb/Blancoynegro.html')

def userList(request):
    users=User.objects.all()
    return render(request,'AppWeb/userList.html', {"users":users})

def mensajeUserList(request):  
    mensajesUsers=MensajeUser.objects.filter(user=request.user.id)
    return render(request,'AppWeb/mensajeUserList.html', {"mensajesUsers":mensajesUsers})

def mensajeUserList(request):
    users=User.objects.all()
    mensajesUsers=MensajeUser.objects.filter(user=request.user.id)
    
    diccionarioMensajes = {}
    for mensaje in mensajesUsers:
        if mensaje.user_transmitter not in diccionarioMensajes:
            lista_mensajes = []
            diccionarioMensajes[mensaje.user_transmitter] = lista_mensajes

    return render(request,'AppWeb/mensajeUserList.html', {"mensajesUsers":mensajesUsers, "users":users, "diccionarioMensajes":diccionarioMensajes})

def mensajeUserDetail(request, pk):
    usertra=User.objects.get(id=pk)
    userrec=User.objects.get(id=request.user.id)
    mensajesUsers=MensajeUser.objects.all()
    return render(request,'AppWeb/mensajeUserDetail.html', {"mensajesUsers":mensajesUsers, "usertra":usertra, "userrec":userrec})

#BLOG
class BlogCreate(CreateView):
    model=Blog
    success_url=reverse_lazy("blogList")
    fields=['imagen', 'titulofoto', 'titulomessage', 'message']
    def form_valid(self, form):
       form.instance.user = self.request.user
       form.instance.imagen = self.request.FILES['imagen']
       return super(BlogCreate, self).form_valid(form)

class BlogList(ListView):
    model=Blog
    template_name='AppWeb/blogList.html'

class BlogDetail(DetailView):
    model=Blog
    template_name=('AppWeb/blogDetail.html')

class BlogUpdate(UpdateView):
    model=Blog
    template_name='AppWeb/blogUpdate.html'
    success_url=reverse_lazy("blogList")
    fields=['titulofoto', 'titulomessage', 'message']

class MensajeCreate(CreateView):
    model=Mensaje
    success_url=reverse_lazy("blogList")
    fields=['message']    
    def form_valid(self, form):
        form.instance.blog_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super(MensajeCreate, self).form_valid(form)
    
class BlogDelete(DeleteView):
    model=Blog
    success_url=reverse_lazy("blogList")

class MensajeUserCreate(CreateView):
    model=MensajeUser
    success_url=reverse_lazy("userList")
    fields=['message']    
    def form_valid(self, form):
        form.instance.user_id=self.kwargs['pk']
        form.instance.user_transmitter=self.request.user        
        return super(MensajeUserCreate, self).form_valid(form)

