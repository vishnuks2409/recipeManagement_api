# Generated by Django 5.0.4 on 2024-05-06 09:03

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('recipe_ingredients', models.CharField(max_length=50)),
                ('instructions', models.TextField()),
                ('recipe_cuisine', models.CharField(max_length=50)),
                ('meal_type', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('comment', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipe_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
