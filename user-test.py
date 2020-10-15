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

    def test_add_existing_credentials(self):
        """
        Test to check if method adds credentials to credentials list
        """
        self.new_user.create_user()
        credentials = Credentials("Instagram", "victor", "pass")
        self.new_user.add_existing_credentials(credentials)

        self.assertEqual(len(self.new_user.credentials), 1)
        self.assertEqual(
            self.new_user.credentials[0].account_name, "Instagram")
        self.assertEqual(self.new_user.credentials[0].user_name, "victor")
        self.assertEqual(self.new_user.credentials[0].password, "pass")

    def test_generate_new_password(self):
        """
        Test to check if proper new password is being generated"
        """
        password = User.generate_new_password()
        self.assertNotEqual(password, "")
        self.assertEqual(len(password), 8)

    def test_add_new_credentials(self):
        """
        Test to check if methods creates new credentials properly
        """
        self.new_user.create_user()
        credentials = Credentials("Twitter", "victormainak")
        self.new_user.add_new_credentials(credentials)

        self.assertEqual(len(self.new_user.credentials), 1)
        self.assertEqual(self.new_user.credentials[0].account_name, "Twitter")
        self.assertEqual(
            self.new_user.credentials[0].user_name, "victormainak")
        self.assertNotEqual(self.new_user.credentials[0].password, "")

    def test_mulitple_credentials(self):
        """
        Test to check if multiple credentials can be added
        """
        credentials_1 = Credentials("Instagram", "victormainak")
        credentials_2 = Credentials("Twitter", "victorkmaina", "password")
        self.new_user.add_new_credentials(credentials_1)
        self.new_user.add_existing_credentials(credentials_2)

        self.assertEqual(len(self.new_user.credentials), 2)

    def test_view_all_credentials(self):
        """
        Test to check if method returns list of all credentials
        """
        credentials_1 = Credentials("Instagram", "victormainak")
        credentials_2 = Credentials("Twitter", "victorkmaina", "password")
        self.new_user.add_new_credentials(credentials_1)
        self.new_user.add_existing_credentials(credentials_2)
        self.new_user.create_user()

        self.assertEqual(
            User.users[0].view_all_credentials(), User.users[0].credentials)

    # def test_find_credentials(self):
    #     """
    #     Test to check if method finds correct login credentials
    #     """
    #     credentials_1 = Credentials("Instagram", "victormainak")
    #     credentials_2 = Credentials("Twitter", "victorkmaina", "password")
    #     self.new_user.add_new_credentials(credentials_1)
    #     self.new_user.add_existing_credentials(credentials_2)

    #     self.new_user.find_credentials("Instagram")

    #     self.assertTrue()

    def test_validate_user(self):
        """
        Test to check if user login info exists
        """

        self.new_user.create_user()
        test_user = User("test", "pass")
        test_user.create_user()

        search_user = User.validate_user("test", "pass")

        self.assertEqual(search_user, User.users[1])
        # self.assertEqual(search_user, User.users[1])
        self.assertTrue(search_user)

    def test_list_users(self):
        """
        Test method to check if it lists all signed in users
        """
        self.new_user.create_user()
        test_user = User("123", "123")
        test_user.create_user()
        user_names = User.list_users()

        # self.assertEqual(search_user, User.users[0])
        self.assertEqual(user_names, [User.users[0].user_name, User.users[1].user_name])

        


if __name__ == "__main__":
    unittest.main()
