from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from watchlist.models import WatchList, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


class StreamPlatformApiView(APIView):

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class StreamPlatformDetailApiView(APIView):

    def _find_by_pk(self, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
            return stream_platform
        except StreamPlatform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        stream_platform = self._find_by_pk(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)

    def update(self, request, pk):
        stream_platform = self._find_by_pk(pk=pk)
        serializer = StreamPlatformSerializer(
            stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stream_platform = self._find_by_pk(pk=pk)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListApiView(APIView):

    def get(self, request):
        items = WatchList.objects.all()
        serializer = WatchListSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailApiView(APIView):

    def _find_by_pk(self, pk):
        try:
            item = WatchList.objects.get(pk=pk)
            return item
        except WatchList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        item = self._find_by_pk(pk=pk)
        serializer = WatchListSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk):
        item = self._find_by_pk(pk=pk)
        serializer = WatchListSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self._find_by_pk(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
