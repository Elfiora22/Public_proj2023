from django.urls import path
from .views import *


urlpatterns = [
    # path('', index),


#paths for json views
    #path('goods/', product_list),
    #path('good/<int:product_id>/', retrieve_product),
    #path('good/delete/<int:product_id>/', delete_product),


#paths for DRF APIViews
#Product paths
    path('all/', ProductList.as_view(), name="list_of_products"),
    path('get/<int:pk>/', ProductRetrieve.as_view(), name="product_find"),
    path('product-create/', CreateProduct.as_view(), name="product_create_post"),
    path('get/<int:pk>/delete/', ProductRetrieveDestroy.as_view(), name="category_find_delete"),
    path('<int:pk>/update/', ProductUpdate.as_view(), name="update_prod_patch_put"),

#Category paths
    # path('category/list/', CategoryList.as_view(), name="categories_list"),
    # path('category/get/<int:pk>/', CategoryRetrieve.as_view(), name="find_category"),
    # path('category/create/', CreateCategory.as_view(), name="create_category"),
    # path('category-upd/<int:pk>/update/', CategoryUpdate.as_view(), name="category_update"),
    # path('category-off/get/<int:pk>/delete/', CategoryRetrieveDestroy.as_view(), name="category_find_delete"),
  

#Brand paths
    # path('brand/list/', BrandList.as_view(), name="list_of_brands"),
    # path('brand/get/<int:pk>/', BrandRetrieve.as_view(),name="find_brand"),
    # path('brand/get/<int:pk>/update/', BrandRetrieveUpdate.as_view(), name="update_put_patch"),
    # path('brand/delete/<int:pk>/', BrandDestroy.as_view(), name="brand_delete"),
    # path('brand-create/', CreateBrand.as_view(), name="brand_create_post") 

]