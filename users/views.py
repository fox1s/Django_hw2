from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from users.models import UserModel
from users.serializers import UserSerializer


class ListCreateView(APIView):
    def get(self, *args, **kwargs):
        db_users = UserModel.objects.all()
        data = UserSerializer(db_users, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        user = get_object_or_404(UserModel.objects.all(), pk=pk)
        print(user)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)

# class UserView(APIView):
#
#     def get(self, *args, **kwargs):
#         return Response('get')
#
#     def post(self, *args, **kwargs):
#         return Response('post')
#
#     def put(self, *args, **kwargs):
#         return Response('put')
#
#     def patch(self, *args, **kwargs):
#         return Response('patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('delete')
