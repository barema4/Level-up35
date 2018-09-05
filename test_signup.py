import unittest
from signup import Signup
class SignupTest(unittest.TestCase):
    def setUp(self):
        self.signup = Signup()
    def test_signup_creation(self):
        self.assertIsInstance(self.signup, Signup)
    
    
    def test_add_user(self):
        
        self.signup.add("sam rub", "mypass123")
        self.assertEqual(len(self.signup.user_bio), 1)

    def test_return_password(self):

        self.signup.add("john", "1234")
        self.assertEqual(self.signup.get_password("john"),'1234')

    def test_missing_key(self):
        
        with self.assertRaises(KeyError):
           self.signup.get_password("jon")

    def test_length(self):
        
        self.assertEqual(self.signup.get_length(), 0)
        self.signup.add("sam rub", "mypass123")
        self.assertEqual(self.signup.get_length(), 1) 