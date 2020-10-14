class User:
    """
    Class to define methods and properties of users
    """
    users = []

    def __init__(self, user_name, password, credential):
        """
        Define username and password properties
        """
        self.user_name = user_name
        self.password = password
        self.credential = credential
    
    def create_user(self):
        User.users.append(self)