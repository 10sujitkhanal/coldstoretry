from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)