from rest_framework import serializers
from rest_framework.validators import ValidationError
from flights.models import Flight
from django.contrib.auth.models import User

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # fields = ['username', 'first_name', 'last_name', 'email', 'password', 'groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'last_login', 'date_joined']
        fields = ['username', 'password']
    # def validate(self, attrs):
    #     email_exists = User.objects.filter(email=attrs['email']).exists()
    #     if email_exists:
    #         raise ValidationErrror("Email already in use!")
    #     return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def __str__(self):
        return self.username
    

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
