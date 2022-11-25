#!/usr/bin/python3
import unittest

from function import modulo

class TestSum(unittest.TestCase):
	def test_1(self):
		x1 = 1
		y1 = 2
		result = modulo(x1, y1)
		self.assertEqual(result, 1)
		
	def test_2(self):
		x2 = 2
		y2 = 3
		result = modulo(x2, y2)
		self.assertEqual(result, 2)

	def test_3(self):
		x3 = 3
		y3 = 2
		result = modulo(x3, y3)
		self.assertEqual(result, 1)

	def test_4(self):
		x4 = 10
		y4 = 5
		result = modulo(x4, y4)
		self.assertEqual(result, 200) 

	def test_5(self):
		x5 = 9
		y5 = 4
		result = modulo(x5, y5)
		self.assertEqual(result, 0)

if __name__ == '__main__':
	unittest.main()