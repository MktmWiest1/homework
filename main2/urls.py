from django.urls import path
from . import views

urlpatterns = [
    path('director/', views.DirectorListCreateAPView.as_view()),
    path('director/<int:id>/', views.DirectorUpdateDeleteAPView.as_view()),
    path('movie/', views.MovieListCreateAPView.as_view()),
    path('movie/<int:id>/', views.MovieUpdateDeleteAPView.as_view()),
    path('review/', views.ReviewListCreateAPView.as_view()),
    path('review/<int:id>/', views.ReviewUpdateDeleteAPView.as_view())
]
