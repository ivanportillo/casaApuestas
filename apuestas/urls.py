from django.conf.urls import patterns, url
from apuestas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^salir/', views.salir, name='salir'),
    url(r'^registro/', views.registro, name='registro'),
    url(r'^ingresar/', views.ingresar, name='ingresar'),
    url(r'^perfil/', views.perfil, name='perfil'),
    url(r'^resultados/', views.resultados, name='resultados'),
    url(r'^apuesta/(?P<idApuesta>\d+)/$', views.apuesta, name='apuesta'),
    url(r'^deporte/(?P<idDeporte>\d+)/$', views.deporte, name='deporte')
)
