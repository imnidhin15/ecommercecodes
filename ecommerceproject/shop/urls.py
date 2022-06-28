from django.urls import path
from .import views
app_name = 'shop'


urlpatterns = [

    path('', views.AllproductCat, name='AllproductCat'),
    path('<slug:c_slug>/', views.Product_list, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.Productdetail, name='prodCatDetail'),

]