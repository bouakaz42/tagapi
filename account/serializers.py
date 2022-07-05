from rest_framework import serializers 
from .models import NewUser

class RgisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['full_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # overide save method to validate the abova other_fields
    def create(self, validated_data):
        user = NewUser(email=validated_data['email'],
                        username=validated_data['username'],
                        full_name=validated_data['full_name'],
                        is_active=True )

        password = validated_data['password']
        user.set_password(password)
        user.save()
        return user
