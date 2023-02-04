from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model 
from rest_framework import serializers

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','last_name','first_name', 'email','password','date_joined')
        extra_kwargs = {'password': {'write_only': True}}

class UserRegisterSerializer(ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ('username','password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
