from django.urls import path

from .views import (StreamPlatformApiView, StreamPlatformDetailApiView,
                    WatchListApiView, WatchListDetailApiView)

urlpatterns = [
    path("streamPlatforms/", StreamPlatformApiView.as_view()),
    path("streamPlatforms/<int:pk>", StreamPlatformDetailApiView.as_view()),

    path("watchLists/", WatchListApiView.as_view()),
    path("watchLists/<int:pk>", WatchListDetailApiView.as_view()),
]
