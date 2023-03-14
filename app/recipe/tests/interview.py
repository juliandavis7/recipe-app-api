from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from rest_framework.test import APIClient
from core.models import Recipe
from recipe.serializers import RecipeSerializer

"""Helper functions"""
def create_user(**params):
  """Create and return a new user."""
  return get_user_model().objects.create_user(**params)

def create_recipe(user, **params):
  """Create and return a sample recipe"""
  defaults = {
    'title': 'Sample recipe title',
    'time_minutes': 10,
    'price': Decimal('10'),
    'description': 'Sample description',
    'link': 'http://example.com/recipe.pdf'
  }
  defaults.update(params)

  recipe = Recipe.objects.create(user=user, **defaults)
  return recipe

"""Test class"""
class PrivateRecipeApiTests(TestCase):
  """Test authenticated API requests."""
  def setUp(self):
    self.client = APIClient()
    self.user = create_user(email='user@example.com', password='testpass123')
    self.client.force_authenticate(self.user)

  """Test method"""
  def test_do_something(self):
    """Does something"""
    create_recipe(user=self.user)
    create_recipe(user=self.user)

    res = self.client.get('/recipes/')

    recipes = Recipe.objects.all().order_by('-id')
    serializer = RecipeSerializer(recipes, many=True)
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)

