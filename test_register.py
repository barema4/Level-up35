import unittest

from register import Registration

class RegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Registration()
    def test_signup_creation(self):

        self.assertIsInstance(self.app, Registration)
    
    def test_length(self):
        
        self.assertEqual(len(self.app.data), 0)

        self.app.add("rubarema", "sam")
        self.assertEqual(len(self.app.data), 1)


    def test_return_lastname(self):

        self.app.add("rubarema", "sam")
        self.assertEqual(self.app.get_lastname("rubarema"),'sam')

    def test_missing_key(self):
        
        with self.assertRaises(KeyError):
           self.app.get_lastname("sum")
    
    def test_username(self):
        self.f = self.app.add_credentials("barema4", "12355")
        self.assertEqual(self.f, ('barema4', '12355'))
    

    def test_contact(self):
        self.address = self.app.add_address("samrubarema6@gmail.com", "+256786666349")
        self.assertEqual(self.address, ('samrubarema6@gmail.com', '+256786666349'))
    
