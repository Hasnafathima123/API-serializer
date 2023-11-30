from django. urls import path
from . import views
urlpatterns=[
    path("",views.index, name="index"),
    path("detial/<int:id>/",views.detial,name="detial"),

]