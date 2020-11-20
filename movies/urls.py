from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from . import api

urlpatterns = format_suffix_patterns([
    path('movie/', views.MovieViewSet.as_view({'get': 'list'})),
    path('movie/<int:pk>/', views.MovieViewSet.as_view({'get': 'retrieve'})),

    path('review/', views.ReviewViewSet.as_view({'post': 'create'})),
    # path('review/<int:pk>/', views.ReviewDestroyView.as_view()),

    path('rating/', views.AddStarRatingViewSet.as_view({'post': 'create'})),
    path('actors/', views.ActorsViewSet.as_view({'get': 'list'})),
    path('actors/<int:pk>/', views.ActorsViewSet.as_view({'get': 'retrieve'})),
])

# urlpatterns = [
#     path('movie/', views.MovieListView.as_view()),
#     path('movie/<int:pk>/', views.MovieDetailView.as_view()),
#
#     path('review/', views.ReviewCreateView.as_view()),
#     # path('review/<int:pk>/', views.ReviewDestroyView.as_view()),
#
#     path('rating/', views.AddStarRatingView.as_view()),
#     path('actors/', views.ActorListView.as_view()),
#     path('actors/<int:pk>', views.ActorDetailView.as_view()),
# ]