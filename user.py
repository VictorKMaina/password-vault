class User:
    """
    Class to define methods and properties of users
    """
    users = []

    def __init__(self, user_name, password, credentials=[]):
        """
        Define username and password properties
        """
        self.user_name = user_name
        self.password = password
        self.credentials = credentials
    
    def create_user(self):
        User.users.append(self)
        
    def add_credentials(self, credentials):
        self.credentials.append(credentials)