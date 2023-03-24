from django.urls import path
from .views import PruebaView,CategoriaView


urlpatterns =[
    path('prueba',PruebaView.as_view()),
    path('otra_prueba',PruebaView.as_view()),
    path('categoria',CategoriaView.as_view())
] 