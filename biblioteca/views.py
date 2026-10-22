from datetime import date, timedelta

from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Emprestimo, Livro, Membro


def lista_livros(request):
    busca = request.GET.get('busca', '')
    livros = Livro.objects.all()

    if busca:
        livros = livros.filter(titulo__icontains=busca)

    contexto = {
        'livros': livros,
        'membros': Membro.objects.all(),
        'emprestimos': Emprestimo.objects.filter(status='ATIVO'),
        'busca': busca,
    }

    return render(request, 'biblioteca/lista_livros.html', contexto)


def emprestar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == 'POST':
        if livro.copias_disponiveis <= 0:
            messages.error(
                request, f'Sem cópias disponíveis de "{livro.titulo}".'
            )
        else:
            membro = get_object_or_404(
                Membro, pk=request.POST.get('membro_id')
            )

            Emprestimo.objects.create(
                livro=livro,
                membro=membro,
                data_prevista_devolucao=date.today() + timedelta(days=14),
            )

            livro.copias_disponiveis -= 1
            livro.save()

            messages.success(
                request, f'Empréstimo de "{livro.titulo}" registrado!'
            )

    return redirect('lista_livros')


def devolver_livro(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, pk=emprestimo_id)

    if request.method != 'POST':
        return redirect('meus_emprestimos', membro_id=emprestimo.membro.id)

    if emprestimo.status == 'DEVOLVIDO':
        messages.warning(request, 'Este livro já foi devolvido.')
    else:
        emprestimo.data_devolucao = date.today()
        emprestimo.status = 'DEVOLVIDO'
        emprestimo.save()

        emprestimo.livro.copias_disponiveis += 1
        emprestimo.livro.save()

        messages.success(
            request, f'Devolução de "{emprestimo.livro.titulo}" registrada!'
        )

    return redirect('meus_emprestimos', membro_id=emprestimo.membro.id)


def meus_emprestimos(request, membro_id):
    membro = get_object_or_404(Membro, pk=membro_id)

    emprestimos = membro.emprestimo_set.order_by('-data_emprestimo')

    return render(
        request,
        'biblioteca/meus_emprestimos.html',
        {
            'membro': membro,
            'emprestimos': emprestimos,
        },
    )


def emprestimos_atrasados(request):
    emprestimos = Emprestimo.objects.filter(
        status='ATIVO',
        data_prevista_devolucao__lt=date.today(),
    ).select_related('livro', 'membro')

    return render(
        request,
        'biblioteca/emprestimos_atrasados.html',
        {'emprestimos': emprestimos},
    )


def relatorio_livros(request):
    livros = Livro.objects.annotate(
        total_emprestimos=Count('emprestimo')
    ).order_by('-total_emprestimos')

    return render(
        request,
        'biblioteca/relatorio_livros.html',
        {'livros': livros},
    )