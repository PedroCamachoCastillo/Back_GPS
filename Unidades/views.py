from django.shortcuts import render, get_object_or_404

# ------------MODELOS---------------
from Unidades.models import Unidades

# --------------SERIALIZERS-----------
from Unidades.serializers import UnidadesSerializers

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from django.http import Http404

# Create your views here.
class UnidadesList(APIView):
    def get(self, request, format=None):
        queryset = Unidades.objects.all()
        serializer = UnidadesSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UnidadesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            response = datas
            return Response (response, status=status.HTTP_201_CREATED)
        response = serializer.errors
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        unidades = get_object_or_404(Unidades.object.all(), pk = pk)
        data = request.data
        serializer = UnidadesSerializers(instance = unidades, data = data, partial=True)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
        response = "La unidad ", pk, " ha sido actualizado exitosamente"
        return Response(response)

    def delete(self, request, pk):
        unidades = get_object_or_404(Unidades.object.all(), pk = pk)
        unidades.delete()
        response = "La unidad ", pk, " ha sido eliminado exitosamente."
        return Response(response, status=status.HTTP_201_CREATED)