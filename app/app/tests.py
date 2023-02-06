"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CaclTests(SimpleTestCase):
  """Test the calc module"""

  def test_add_numbers(self):
    """Test adding numbers together"""
    res = calc.add(6, 5)
    self.assertEqual(res, 11)

  def test_subtract_numbers(self):
    res = calc.subtract(6, 5)
    self.assertEqual(res, 1)