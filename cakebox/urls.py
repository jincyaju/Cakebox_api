"""cakebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cakeapp import views

from django.conf import settings
from django.conf.urls.static import static


from cakeapi import views as api_views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api/cakes",api_views.CakeView,basename="cakes")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cake/add/',views.CakeCreateView.as_view(),name="cake-add"),
    path('cake/all/',views.CakeListView.as_view(),name="cake-list"),
    path('cake/<int:pk>',views.CakeDetailsView.as_view(),name="cake-detail"),
    path('cake/<int:pk>/remove/',views.CakeDetailsView.as_view(),name="cake-delete"),
    path('cake/<int:pk>/change/',views.CakeEditView.as_view(),name="cake-edit"),
    path('cake/register/',views.SignUpView.as_view(),name="register"),
    path('login/',views.SignInView.as_view(),name="signin"),



]+router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

