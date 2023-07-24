import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from produto.models import Produto


class Utils:
    @staticmethod
    def gen_digits(max_lenght):
        return str(''.join(choice(string.digits) for i in range(max_lenght)))
    

class ProdutoClass:
    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random()*randint(10, 50),
                estoque=randint(10,200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'Computador',
    'Mouse',
    'Teclado',
    'Monitor',
    'Mousepad',
    'Impressora',
    'Scanner',
    'Notebook',
    'Webcam',
    'Roteador',
    'Switch',
    )

tic = timeit.default_timer()
ProdutoClass.criar_produtos(produtos)
toc = timeit.default_timer()

print('Tempo:', toc - tic)