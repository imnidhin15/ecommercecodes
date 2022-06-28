from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

#
# # Create your views here.
# def SearchResults(request):
#     products = None
#     query = None
#     search = request.GET.get('search')
#     if search:
#         products = Product.objects.filter(
#             Q(name__contains=search) |
#             Q(description__contains=search)
#         )
#         paginator = Paginator(products, 8)
#         try:
#             page = int(request.GET.get('page', '1'))
#         except:
#             page = 1
#         try:
#             products = paginator.page(page)
#         except (EmptyPage, InvalidPage):
#             products = paginator.page(paginator.num_pages)
#     return render(request, 'product_list.html', {'products': products})
