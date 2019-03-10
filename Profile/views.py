from django.shortcuts import render, get_object_or_404

# ------------MODELOS---------------
from Profile.models import Profile

# --------------SERIALIZERS-----------
from Profile.serializers import ProfileSerializers

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from django.http import Http404

# Create your views here.
class ProfileList(APIView):
    def get(self, request, format=None):
        queryset = Profile.objects.all()
        serializer = ProfileSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response(response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        profile = get_object_or_404(Profile.object.all(), pk = pk)
        data = request.data
        serializer = ProfileSerializers(instance = profile, data = data, partial=True)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
        response = "El perfil ", pk, " ha sido actualizado exitosamente"
        return Response(response)

    def delete(self, request, pk):
        profile = get_object_or_404(Profile.object.all(), pk = pk)
        profile.delete()
        response = "El perfil ", pk, " ha sido eliminado exitosamente."
        return Response(response, status=status.HTTP_201_CREATED)