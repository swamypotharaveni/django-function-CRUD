from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('shop',views.index),
    path('list',views.list),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
    path('signup/',views.signup.as_view(),name='signup'),
    path('details/<int:pk>',views.details.as_view(),name='details'),
]
