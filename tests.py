from fuzzy import fuzzy_match_simple
import unittest


class TestMain(unittest.TestCase):
	
	def test_fuzzy_match_simple(self):
		self.assertEqual(fuzzy_match_simple('leta', 'leta'), 0)

	def test_substitution(self):
		self.assertEqual(fuzzy_match_simple('leda', 'leta'), 1)

	def test_addition_or_deletion(self):
		self.assertEqual(fuzzy_match_simple('retal', 'rettal'), 1)
		self.assertEqual(fuzzy_match_simple('leeta', 'leta'), 1)

	def test_edge_cases(self):
		self.assertEqual(fuzzy_match_simple('leta', ''), 4)
		self.assertEqual(fuzzy_match_simple('',''), 0)





if __name__ == '__main__': 
	unittest.main()