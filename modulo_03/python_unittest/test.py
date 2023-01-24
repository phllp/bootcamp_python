import unittest
from root_square_solver import root_square_solver

class check_root_square_solver(unittest.TestCase):
  def test_check_two_roots(self):
    response = root_square_solver(1, -5, 6)
    self.assertEqual(len(response), 2)

  def test_check_root_value(self):
    response = root_square_solver(1, -5, 6)
    self.assertIn(response[0], [2,3])
    self.assertIn(response[1], [2,3])
  
  def test_check_one_root(self):
    response = root_square_solver(1, -4, 4)
    self.assertEqual(len(response), 1)
