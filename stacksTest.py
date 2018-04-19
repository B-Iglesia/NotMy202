import stacks
import unittest
class TestCases(unittest.TestCase):
	def test_init1(self):
		a = Stack(50)
		self.assertEqual(a, [None] * 50)
	def test_init2(self):
		a = Stack(30)
		self.assertEqual(a, [None] * 30)
	
	

if __name__ == "__main__":
	unittest.main()
	
