"""
URL configuration for recipe project.

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
# from . import views
from vege import views
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',home,name="home"),
    path('recipes/',recipes,name="recipes"),
    path('login/',login_page,name="login_page"),
    path('logout/', views.logout_view, name='logout'),
    path('register/',register_page,name="register_page"),
    path('profile/',profile,name="profile"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('success-page',success_page,name="success_page"),
    path('admin/', admin.site.urls),
    path('delete-recipe/<int:id>/',views.delete_recipe,name='delete_recipe'),
    path('update/<int:id>/',views.update,name='update'),
    path('update-recipe/<int:id>/',views.update_recipe,name='update_recipe'),
    path('update-profile-photo/', views.update_profile_photo, name='update-profile-photo'),



]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()
