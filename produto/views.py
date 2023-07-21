from django.shortcuts import render
from .models import Produto

def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    print(objects)
    context = {'produtos': objects}
    return render(request, template_name, context)
