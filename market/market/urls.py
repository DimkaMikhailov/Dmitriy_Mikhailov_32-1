"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from market.settings import MEDIA_URL, MEDIA_ROOT

from first_views import views as first_views
from goods import views as products_vies

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello', first_views.helo),
    path('date_now', first_views.date_now),
    path('buy', first_views.buy),

    path('', products_vies.index),
    path('products/', products_vies.products),
    path('products/<int:product_id>/', products_vies.product_card),
    path('categories/', products_vies.categories),
    path('category/<int:category_id>/', products_vies.category_card),

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
