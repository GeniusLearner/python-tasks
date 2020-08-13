from django.shortcuts import redirect

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response
