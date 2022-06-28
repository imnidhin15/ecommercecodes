from django.db.models import Q
from django.shortcuts import HttpResponse, get_object_or_404, render
from .models import Category, Product
from django.core.paginator import EmptyPage, InvalidPage, Paginator


# Create your views here.
def index(request):
    return HttpResponse('hai')


def AllproductCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)
    paginator = Paginator(products_list, 8)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page})

def Productdetail(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})


def Product_list(request, c_slug):

    products_list = None
    search = request.GET.get('search')
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)
    if search:
        products_list = products_list.filter(
            Q(name__contains=search) |
            Q(description__contains=search)
        )
    paginator = Paginator(products_list, 8)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'products': products})
