from django.urls import url
from . import views
urlpatterns=[
    url('movies/', views.movies, name=''),
    url('movie_details/<int:post_idx>', views.movie_details, name='movie_details')
]