from django.urls import include, path
from estoque import views

app_name = 'estoque'


entrada_patterns = [
    path('', views.EstoqueEntradaList.as_view(), name='estoque_entrada_list'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),
]
    

saida_patterns = [
    path('', views.EstoqueSaidaList.as_view(), name='estoque_saida_list'),
    path('add/', views.estoque_saida_add, name='estoque_saida_add'),
]


urlpatterns = [
    path('<int:pk>/', views.EstoqueDetail.as_view(), name='estoque_detail'),
    path('entrada/', include(entrada_patterns)),
    path('saida/', include(saida_patterns)),
]