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

    option = input()

    if option == "1":
        print("\n" + "Create a user name:")
        user_name = input()

        print("\n" + "Create new password:")
        password = input()

        create_new_account(user_name, password)
    else:
        print("OK")


if __name__ == "__main__":
    main()
