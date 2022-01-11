from django.shortcuts import render, HttpResponse
from blog.models import Categoria, Post 


def blogging(request):
    blog = Post.objects.all()
    return render(request,"blog/blog.html",{'blog':blog})

def categoria(request, categoria_id):
    categoria =  Categoria.objects.get(id=categoria_id)
    blog = Post.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html",{'categoria':categoria,'blog':blog})
