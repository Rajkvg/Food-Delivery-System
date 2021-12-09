from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('order/', views.order, name="order"),
    path('item/<int:number>',views.item,name="item")
]
urlpatterns+=staticfiles_urlpatterns()