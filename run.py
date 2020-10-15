#!/usr/bin/env python3.9

from user import User
from credentials import Credentials

def create_new_account(user_name, password):
    new_account = User(user_name, password)
    new_account.create_user()


def main():
    print("Welcome to PassLocker.\n" + "1. Create New Account\n" + "2. Log In")

    print("\n")
    print("Choose an option:")

    while True:
        option = input()
    
        if option == "1":
            while True:
                print("\n" + "Create a user name:")
                user_name = input()
        
                print("\n" + "Create new password:")
                password = input()
        
                create_new_account(user_name, password)
                break
            print("\n")
            print(f"Welcome, {user_name}. Pick an option:\n" + "1. Add existing credentials \n" + "2. Create new credentials")

        elif option == "2":
            print("OK")
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
