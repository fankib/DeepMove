import unittest

from sparse_traces import Gowalla

class GowallaTest(unittest.TestCase):
    
    def test_run(self):
        data_generator = Gowalla('small-10000.txt', 101, 6)
        data_generator.run()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()