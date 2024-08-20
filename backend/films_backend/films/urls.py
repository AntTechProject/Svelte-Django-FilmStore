from django.urls import path
from  rest_framework.routers import DefaultRouter
# from films.views import FilmListAPIView, FilmDetailAPIView
from films.views import FilmViewSet

# urlpatterns = [
#     path('films/', FilmListAPIView.as_view()),
#     path('films/<int:pk>', FilmDetailAPIView.as_view()),
# ]

router = DefaultRouter()
router.register('films', FilmViewSet, basename = 'films')
urlpatterns = router.urls