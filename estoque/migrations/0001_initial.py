# Generated by Django 4.2.3 on 2023-07-17 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produto', '0002_remove_produto_numero_serie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('nf', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='nota fiscal')),
                ('movimento', models.CharField(blank=True, choices=[('e', 'entrada'), ('s', 'saida')], max_length=1)),
                ('funcionario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='EstoqueItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveBigIntegerField()),
                ('saldo', models.PositiveBigIntegerField()),
                ('estoque', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='estoque.estoque')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
