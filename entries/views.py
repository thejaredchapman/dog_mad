from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView

from serializers import MyPhotoSerializer
# Create your views here.


class PhotoList(APIView):
    def post(self, request, format=None):
        serializer = MyPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)