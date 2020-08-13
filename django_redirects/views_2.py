from django.shortcuts import redirect

def model_redirect_view(request):
    product = Product.objects.filter(featured=True).first()
    return redirect(product)

    # redirect will call product.get_absolute_url() and use the result as redirect target



# Passing a url name and arguments

from django.shortcuts import redirect

def fixed_featured_product_view(request):
    product_id = settings.FEATURED_PRODUCT_ID
    return redirect('product_detail, product_id=product_id')


    # Passing a URL

from django.shortcuts import redirect

def featured_product_view(request):
    return redirect('/products/42/') # redirect() will treat / or . as a URL and use it as redirect target.


#urls.py
from django.urls import path
from .views import SearchRedirectView

urlpatterns = [
    path('/search/<term>/', SearchRedirectView.as_view())
]

#views.py
from django.views.generic.base import RedirectView

class SearchRedirectView(RedirectView):
    url = 'https://google.com/?q=%(term)s'

#Same case with little modification

#urls.py
from django.views.generic.base import RedirectView

urlpatterns = [
    path('/search/<term>/',
    RedirectView.as_view(url='https://google.com/?q=%(term)s'))
]

#For custom behaviour

from random import choice
from django.views.generic.base import RedirectView

class RandomAnimalView(RedirectView):
    animal_urls = ['/dog/', '/cat/', '/parrot']
    is_permanent = from django.utils.translation import ugettext_lazy as _

    def get_redirect_url(*args, **kwargs):
        return choice(self.animal_urls)

        #Another case

from random import choice
from django.shortcuts import redirect

def random_animal_view(request):
    animal_urls = ['/dog/','/cat/', '/parrot/']
    return redirect(choice(animal_urls))


#Let’s assume you want to redirect from some_view() to product_view(), but pass an optional parameter category:

from django.urls import reverse
from urllib.parse import urlencode

def some_view(request):
    ...
    base_url = reverse('product_view')
    query_string = urlencode({'category': category.id})
    url = '{}?{}'.format(base_url, query_string)
    return redirect(url)

def product_view(request):
    category_id = request.GET.get('category')

class HttpResponseTemporaryRedirect(HttpResponseRedirectBase):
    status_code = 307

def temporary_redirect_view(request):
    response = redirect('success_view')
    response.status_code = 307
    return response


def product_view(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return redirect('/')
    return render(request, 'product_detail.html', {'product': product})


def get_product_or_redirect(product_id):
    try:
        return Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return redirect('/')

def product_view(request, product_id):
    product = get_product_or_redirect(product_id)
    return render(request, 'product_detail.html', {'product': product})


#import the fumction first
from django.utils.http import is_safe_url
is_safe_url('/profile/')



