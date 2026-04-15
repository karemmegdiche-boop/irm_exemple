import unittest

from mon_module import une_fonction

class TestMonModule(unittest.TestCase):
    def test_une_fonction(self):
        self.assertEqual(une_fonction(2, 3), 5)

    def test_une_fonction2(self):
        self.assertEqual(une_fonction2(2, 3), -1)
        
if __name__ == '__main__':
    unittest.main()
