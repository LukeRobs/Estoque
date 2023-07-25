from django.shortcuts import render
from .models import Estoque


def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
   #objects = Estoque.objects.filter(movimento='e')
    objects = Estoque.objects.all()
    context = {'estoque': objects}
    return render(request, template_name, context)