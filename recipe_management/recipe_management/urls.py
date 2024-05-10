"""
URL configuration for recipe_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from recipe import views
from rest_framework.authtoken import views as rviews



router=DefaultRouter()
router.register('recipe',views.Recipe_viewset),
router.register('register',views.Register_viewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-token-auth/', rviews.obtain_auth_token),
    path('add-review/',views.Create_review.as_view()),
    path('get-review/<int:pk>',views.Detail_review.as_view()),
    path('search/', views.Search_recipe.as_view()),
    path('cuisine/', views.Cuisin_filter.as_view()),
    path('meal/', views.Meal_filter.as_view()),
    path('ingredients/', views.Ingredients_filter.as_view()),

]
