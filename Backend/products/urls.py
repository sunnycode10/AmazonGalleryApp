from django.urls import path, include
from django.urls.resolvers import URLPattern
from rest_framework import routers
from . views import ProductList, CategoryViewSet, SellerViewSet,  ProductListAPIView
from rest_framework.routers import DefaultRouter
# from rest_framework.routers import DefaultRouter =>{ANOTHER WAY TO USE THE VIEWSET} INSTEAD OF THIS =>{
            # category_list = CategoryViewSet.as_view({
                # 'get': 'list',
                # 'post': 'create'
            # })
# }


category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

category_detail = CategoryViewSet.as_view({
    'get':'retrive',
    'put': 'update',
    'delete': 'destroy'
})

# USING ROUTER FOR THE SELLER VIEW
router = DefaultRouter(trailing_slash=False)
router.register('sellers', SellerViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('products/', ProductList.as_view()),
    path('product-filter/', ProductListAPIView.as_view()),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>', category_detail, name='category_detail'),
    # path('sellers', SellerViewSet.as_view())
]