from django.urls import path
from stream.views import *

urlpatterns = [
    path('movies/', MoviesView.as_view(), name="moviesList"),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name="movie-detail")
]
