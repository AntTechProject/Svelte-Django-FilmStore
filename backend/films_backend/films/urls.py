from django.urls import path
from films.views import FilmListAPIView, FilmDetailAPIView

urlpatterns = [
    path('films/', FilmListAPIView.as_view()),
    path('films/<int:pk>', FilmDetailAPIView.as_view()),
]