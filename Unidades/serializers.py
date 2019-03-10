from rest_framework import routers, serializers, viewsets

from Unidades.models import Unidades

class UnidadesSerializers(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.profile = validated_data.get('profile', instance.user)
        instance.plate = validated_data.get('plate', instance.name)
        instance.brand = validated_data.get('brand', instance.address)
        instance.color = validated_data.get('color', instance.phone)
        instance.save()
        return instance

    class Meta:
        model = Unidades
        fields = ('id', 'profile', 'plate', 'brand', 'color')