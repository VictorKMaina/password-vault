from credentials import Credential
import unittest

class TestCredentials(unittest.TestCase):
    """
    Class for testing credentials methods and behaviours
    """
    def setUp(self):
        """
        Create new instance of credential
        """
        self.new_credential = Credential("Instagram", "victormainak", "password")
    
    def test_init_(self):
        """
        Test case to check if new credential has been properly instantiated
        """
        self.assertEqual(self.new_credential.account_name, "Instagram")
        self.assertEqual(self.new_credential.user_name, "victormainak")
        self.assertEqual(self.new_credential.password, "password")

if __name__ == "__main__":
    unittest.main()