from django.urls import path

from web import views

urlpatterns = [
    path('', views.page, name='page'),
    path('<str:slug>', views.redirect_short_url, name='redirect'),
]
