#!/usr/bin/env python3.9

from user import User
from credentials import Credentials

def create_new_account(user_name, password):
    """
    Function for creating a new user
    """
    new_account = User(user_name, password)
    new_account.create_user()

def view_credentials(self):
    """
    Function for listing all credentials
    """



def main():
    current_user = None

    while True:
        print("\nWelcome to PassLocker.\n" + "1. Create New Account\n" + "2. Log In\n" + "3. Show existing users")

        print("\n")
        print("Choose an option:")
        option = input()
    
        if option == "1":
                print("\n" + "Create a user name:")
                new_user_name = input()
        
                print("\n" + "Create new password:")
                new_password = input()
        
                create_new_account(new_user_name, new_password)

        elif option == "2":
            print("\n")
            print("Enter your user name:")
            enter_user_name = input()
            print("Enter your password:")
            enter_password = input()

            current_user = 

            print(f"Welcome, {user_name}.\n" + "1. Add existing credentials \n" + "2. Create new credentials\n" + "3. View existing credentials")
            print("\nPick an option:")

            option = input()

        elif option == "3":
            print("\nExisting Users\n" + "-"*20 + "\n" + str(User.find_user()))
        
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
