from django.http.response import HttpResponse
from rest_framework import generics, filters
from .serializers import *
from .models import *
import json 
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
#from rest_framework.pagination import PageNumberPagination
from .paginations import ProductPagination

 

##### HTTP responses
#def index(request):
    #return HttpResponse('Welcome!')
# def products_page (request):
#     return HttpResponse('Look at this awesome products')
#

#### FUNCTIONS for made-up json views !--> DRF generics are loads better
# LIST
# def product_list(request):
#     products = Product.objects.all()
#     prods_list = []
#     for prod in products:
#         tmp_prod = {
#             "id": prod.id,
#             "title": prod.title,
#             "price": float(prod.price),
#             "old_price": float(prod.old_price),
#             "quantity": prod.quantity,
#             "brand_id": prod.brand_id,
#         }
#         prods_list.append(tmp_prod)
#     return  HttpResponse(json.dumps(prods_list))

# #RETRIEVE
# def retrieve_product(request, product_id):
#     try:
#         product = Product.objects.get(pk=product_id)
#         data = {
#              "id": product.id,
#             "title": product.title,
#             "price": float(product.price),
#             "old_price": float(product.old_price),
#             "quantity": product.quantity,
#             "brand_id": product.brand_id,
#         }
#     except Product.DoesNotExist:
#         data = {"error": "product does not exist"} 
#     return  HttpResponse(json.dumps(data))

# #DELETE
# def delete_product(request, product_id):
#     try:
#         product = Product.objects.get(pk=product_id)
#         data = {
#              "id": product.id,
#             "message": "success",
#         }
#         product.delete()
#     except Product.DoesNotExist:
#         data = {"error": "product does not exist"} 
#     return  HttpResponse(json.dumps(data))   
      
#___________________________________________________________________________#
#Product  DRF APIViews
class ProductList(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset= Product.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ("title", "brand__title")
    #filterset_fields = ("brand_id", "price")
    filterset_class = ProductFilter
    pagination_class = ProductPagination



class ProductRetrieve(generics.RetrieveAPIView):
    serializer_class =  ProductSerializer
    queryset = Product.objects.all()


class CreateProduct(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductUpdate(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()    


class ProductRetrieveDestroy(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


#___________________________________________________________________________#
#Category DRF APIViews
class CategoryList(generics.ListAPIView):
    serializer_class =  CategorySerializer
    queryset = Category.objects.all()

    #def get_queryset(self):
        #return Category.objects.filter(title="Women's Snowboards", is_active=True)
        #SQL SELECT * FROM categories WHERE title="Women's Snowboards" and is_active=True
        #return Category.objects.filter(Q(title="Women's Snowboards") | Q(is_active=True))
        #SQL SELECT * FROM categories WHERE title="Women's Snowboards" or is_active=True
    


# class CategoryRetrieve(generics.RetrieveAPIView):
#     serializer_class =  CategorySerializer
#     queryset = Category.objects.all()


# class CreateCategory(generics.CreateAPIView):
#     serializer_class = CategorySerializer 


# class CategoryUpdate(generics.UpdateAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


# class CategoryRetrieveDestroy(generics.RetrieveDestroyAPIView):
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()


class BrandList(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

# class CreateBrand(generics.CreateAPIView):
#     serializer_class = BrandSerializer    



# class BrandRetrieve(generics.RetrieveAPIView):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()



# class BrandRetrieveUpdate(generics.RetrieveUpdateAPIView):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()



# class BrandDestroy(generics.DestroyAPIView):
#     serializer_class = BrandSerializer
#     queryset = Brand.objects.all()



    





    


        
        



        



