import unittest
from user import User
# from credentials import Credentials

class TestUser(unittest.TestCase):
    """
    Class for testing user class methods
    """
    def setUp(self):
        """
        Create new instance of user
        """
        self.new_user = User("victormainak", "password")

    def test_init(self):
        """
        Test to check if object has been initiated properly
        """
        self.assertEqual(self.new_user.user_name, "victormainak")
        self.assertEqual(self.new_user.password, "password")
    
    def test_create_user(self):
        """
        Test case to check if new user has been created
        """
        self.new_user.create_user()
        self.assertEqual(len(User.users), 1)

if __name__ == "__main__":
    unittest.main()