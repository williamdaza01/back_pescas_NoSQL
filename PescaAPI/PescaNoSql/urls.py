from django.urls import path, re_path
from PescaNoSql import views

urlpatterns=[
    path('metodo/', views.metodoApi),
    path('cuenca/', views.cuencasApi),
    path('pesca/', views.pescasApi),
    re_path(r'^cuenca/([0-9]+)$', views.cuencasApi),
    re_path(r'^metodo/([0-9]+)$', views.metodoApi),
    re_path(r'^pesca/([0-9]+)$', views.pescasApi),
]