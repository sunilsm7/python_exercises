import unittest
from fibonacci import fib

class TestFibonacci(unittest.TestCase):
	def setUp(self):
		self.fib_elems = ((0,0),(1,1), (2,1),(3,2),(4,3),(5,8))
		print("setup executed!")

	def test_calculation(self):
		for (i, val) in self.fib_elems:
			self.assertEqual(fib(i), val)

	def tearDown(self):
		self.fib_elems = None
		print('tearDown executed!')


if __name__ == "__main__": 
    unittest.main()