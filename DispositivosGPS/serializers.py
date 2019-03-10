from rest_framework import routers, serializers, viewsets

from DispositivosGPS.models import DispositivosGPS

class DispositivosGPSSerializers(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.unity = validated_data.get('unity', instance.user)
        instance.name_model = validated_data.get('name_model', instance.name)
        instance.brand = validated_data.get('brand', instance.address)
        instance.serial = validated_data.get('serial', instance.phone)
        instance.save()
        return instance

    class Meta:
        model = DispositivosGPS
        fields = ('id', 'unity', 'name_model', 'brand', 'serial')