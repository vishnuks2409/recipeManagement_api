from rest_framework import serializers
from .models import Recipe,Review
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','recipe_name','recipe_ingredients','instructions','recipe_cuisine','meal_type']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['recipe_name','user','rating','comment']

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']

    def create(self,validate_data):
        user=User.objects.create_user(username=validate_data['username'],
                                      password=validate_data['password'])
        user.save()
        return  user




