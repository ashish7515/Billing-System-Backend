"""
URL configuration for store_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
# from rest_framework_simplejwt.views import Tokenb
from django.contrib import admin
from myapp.views import *
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [ 
    # User authentication URLs...

    # Products
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    # path('users/', UserListView.as_view(), name='user-list'),    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    # path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    # path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    # path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),

    # Customers
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),

    # Billing
    path('bills/', BillList.as_view(), name='bill-list'),
    path('bills/<int:pk>/', BillDetail.as_view(), name='bill-detail'),
    path('bill-items/', BillItemList.as_view(), name='billitem-list'),
    path('bill-items/<int:pk>/', BillItemDetail.as_view(), name='billitem-detail'),
    # path('bill/', BillCreateAPIView.as_view(), name='bill-create'),
    
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name="schema")),

]
