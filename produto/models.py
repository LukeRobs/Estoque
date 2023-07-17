from django.db import models

class produto(models.Model):

    OPCOES = (
        ('Disponivel', 'Disponivel'),
        ('Alocado', 'Alocado'),
        ('Quebrado','Quebrado'),
        ('Manutenção','Manutenção')
    )
    importado = models.BooleanField(default=False)
    numero_serie = models.CharField('SERIE', max_length=15)
    produto = models.CharField(max_length=100, unique=True)
    tombo = models.DecimalField(max_digits=5, decimal_places=0)
    responsavel = models.CharField(max_length=50)
    status = models.CharField(
        max_length=10,
        choices= OPCOES,
    )
    class Meta:
        ordering=('produto',)

    def __str__(self):
        return self.produto

