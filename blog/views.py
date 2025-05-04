from django.shortcuts import render

def index(request):  # Renomeado de 'blog' para 'index'
    print('index')
    return render(
        request,
        'blog/index.html'
    )

def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html'
    )
