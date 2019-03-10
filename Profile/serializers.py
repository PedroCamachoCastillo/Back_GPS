from rest_framework import routers, serializers, viewsets

from Profile.models import Profile

class ProfileSerializers(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.edad = validated_data.get('edad', instance.edad)
        instance.save()
        return instance

    class Meta:
        model = Profile
        fields = ('id','user','name', 'address', 'phone', 'email', 'edad')