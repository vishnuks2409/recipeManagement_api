from django.shortcuts import render
from rest_framework import  viewsets
from .models import Recipe,Review
from django.contrib.auth.models import User
from.serializers import RecipeSerializer,ReviewSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django.db.models import Q


class Recipe_viewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class Create_review(APIView):
    def post(self, request):
        r = ReviewSerializer(data=request.data)
        if r.is_valid():
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Detail_review(APIView):
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        recipe_id=self.get_object(pk)
        review=Review.objects.filter(recipe_name=recipe_id)
        book=ReviewSerializer(review,many=True)
        return Response(book.data)



class Register_viewset(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer

class User_logout(APIView):

    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg': "logout successfully"}, status=status.HTTP_200_OK)

class Search_recipe(APIView):
    def get(self,request):
        query=self.request.query_params.get('search')
        if query:
            recipes = Recipe.objects.filter(Q(recipe_name__icontains=query) | Q(recipe_ingredients__icontains=query))
            b = RecipeSerializer(recipes, many=True)
            return Response(b.data)

#FILTERS
class Cuisin_filter(APIView):
    def get(self,request):
        query=self.request.query_params.get('cuisine')
        if query:
            recipes=Recipe.objects.filter(recipe_cuisine=query)
            r=RecipeSerializer(recipes,many=True)
            return Response(r.data)
class Meal_filter(APIView):
    def get(self,request):
        query=self.request.query_params.get('mealtype')
        if query:
            recipes=Recipe.objects.filter(meal_type=query)
            r=RecipeSerializer(recipes,many=True)
            return Response(r.data)

class Ingredients_filter(APIView):
    def get(self, request):
        query = self.request.query_params.get('cuisine')
        if query:
            recipes = Recipe.objects.filter(recipe_ingredients=query)
            r = RecipeSerializer(recipes, many=True)
            return Response(r.data)



