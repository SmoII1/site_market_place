"""
URL configuration for market_place project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from market_place import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.items, name='main'),
    path('item_card/<str:item_name>/', views.item_card, name='item_card'),
    path('cart/', views.cart, name="cart"),
    path('profile_user/<int:user_id>', views.profile_user, name='profile_user'),
    path('accounts/login/', views.log_in, name='login'),
    path('accounts/logout/', views.log_out, name='logout'),
    path('register/', views.register)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)