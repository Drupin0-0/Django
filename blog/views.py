from django.shortcuts import render

def index(request):  # Renomeado de 'blog' para 'index'
    print('index')
    
    context =   {
            'text': 'estamos na blog',
            'title': 'esse e o site do '
        }
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')
    context =   {
            'text': 'estamos na home'
        }
    return render(
        request,
        'blog/exemplo.html',
        context
    )
