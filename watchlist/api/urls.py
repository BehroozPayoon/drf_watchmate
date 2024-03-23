from django.urls import path

from .views import (StreamPlatformApiView, StreamPlatformDetailApiView,
                    WatchListApiView, WatchListDetailApiView)

urlpatterns = [
    path("streamPlatforms/", StreamPlatformApiView.as_view(),
         name="stream_platforms"),
    path("streamPlatforms/<int:pk>", StreamPlatformDetailApiView.as_view(),
         name="stream_platform_detail"),

    path("watchLists/", WatchListApiView.as_view(), name="watch_list"),
    path("watchlists/<int:pk>", WatchListDetailApiView.as_view(),
         name="watch_list_detail"),
]
