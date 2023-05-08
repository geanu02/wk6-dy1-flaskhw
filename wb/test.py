import unittest
from wb import likes

class TestLikes(unittest.TestCase):
    
    def test_no_likes(self):
        self.assertEqual(likes([]), "no one likes this")
        
    def test_one_like(self):
        self.assertEqual(likes(["Peter"]), "Peter likes this")
        
    def test_two_likes(self):
        self.assertEqual(likes(["Jacob", "Alex"]), "Jacob and Alex like this")
        
    def test_three_likes(self):
        self.assertEqual(likes(["Max", "John", "Mark"]), "Max, John and Mark like this")
        
    def test_four_likes(self):
        self.assertEqual(likes(["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this")
        
    def test_five_likes(self):
        self.assertEqual(likes(["Alice", "Bob", "Charlie", "David", "Eve"]), "Alice, Bob and 3 others like this")
        
if __name__ == '__main__':
    unittest.main()