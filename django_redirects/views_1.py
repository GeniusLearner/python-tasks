def hand_crafted_redirect_view(request):
    response = HttpResponse(status=302)
    response['Location'] = '/redirect/success/'
    return response


    # Second Case

def redirect_view(request):
    return HttpResponseRedirect('/redirect/success/')
