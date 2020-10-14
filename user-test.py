import unittest
from user import User
from credentials import Credentials


class TestUser(unittest.TestCase):
    """
    Class for testing user class methods
    """

    def setUp(self):
        """
        Create new instances of  and credentials
        """
        self.new_credentials = Credentials(
            "Instagram", "victormainak", "password")
        self.new_user = User("victormainak", "password", credentials=[])

    def tearDown(self):
        """
        Reset users list
        """
        User.users = []

    def test_init(self):
        """
        Test to check if object has been initiated properly
        """
        self.assertEqual(self.new_user.user_name, "victormainak")
        self.assertEqual(self.new_user.password, "password")

    def test_add_account(self):
        """
        Test case to check if new account has been created
        """
        self.new_user.create_user()
        self.assertEqual(len(User.users), 1)
    
    def test_multiple_accounts(self):
        """
        Test case to check if another account has been created
        """
        self.new_user.create_user()
        self.test_user = User("user", "pass")
        self.test_user.create_user()
        self.assertEqual(len(User.users), 2)

    def test_add_credentials(self):
        """
        Test to check if method adds credentials to credentials list
        """
        self.new_user.create_user()
        credentials = Credentials("Instagram", "victor", "pass")
        self.new_user.add_credentials(credentials)

        self.assertEqual(self.new_user.credentials[0].account_name, "Instagram")
        self.assertEqual(self.new_user.credentials[0].user_name, "victor")
        self.assertEqual(self.new_user.credentials[0].password, "pass")


if __name__ == "__main__":
    unittest.main()