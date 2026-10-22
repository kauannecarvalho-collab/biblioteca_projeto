from django.contrib import admin
from django.urls import path
from biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_livros, name='lista_livros'),
    path('emprestar/<int:livro_id>/', views.emprestar_livro, name='emprestar_livro'),
    path('devolver/<int:emprestimo_id>/', views.devolver_livro, name='devolver_livro'),
    path('membro/<int:membro_id>/emprestimos/', views.meus_emprestimos, name='meus_emprestimos'),
    path(
    'emprestimos-atrasados/',
    views.emprestimos_atrasados,
    name='emprestimos_atrasados'
),  path('relatorio/', views.relatorio_livros, name='relatorio_livros'),
]

