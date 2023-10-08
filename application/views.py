from django.shortcuts import render


def show_page(request, pk=None):

    return render(request, 'index.html', context={'id': pk})
