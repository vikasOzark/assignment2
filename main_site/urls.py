from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('docs/', views.documentation, name='docs')
]
# hello gg