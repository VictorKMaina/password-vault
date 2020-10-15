#!/usr/bin/env python3.9

from user import User
from credentials import Credentials



def create_new_account(user_name, password):
    """
    Function for creating a new user
    """
    new_account = User(user_name, password, credentials=[])
    new_account.create_user()

def login(user_name, password):
    """
    Function for login in user
    """
    return User.validate_user(user_name, password)

def add_existing_credentials(user, credentials):
    """
    Function for adding existing credentials to user object
    """
    user.add_existing_credentials(credentials)

def list_credentials(user):
    """
    List all saved credentials in user object
    """
    return User.view_all_credentials(user)



def main():
    create_new_account("user", "user")

    while True:
        print("\nWelcome to PassLocker.\n" + "\n1. Create New Account\n" + "2. Log In\n" + "3. Show existing users\n" + "4. Exit PassLocker")

        print("\nChoose an option:")
        option = input()
    
        if option == "1":
                print("\n" + "Create a user name:")
                new_user_name = input()
        
                print("\n" + "Create new password:")
                new_password = input()
        
                create_new_account(new_user_name, new_password)

        elif option == "2":
            while True:
                print("\n")
                print("Enter your user name:")
                enter_user_name = input()
                print("Enter your password:")
                enter_password = input()

                current_user = login(enter_user_name, enter_password)

                if current_user == False:
                    print("\nInvalid username or password. Please try again.")
                else:
                    while True:     
                        print(f"\nWelcome, {current_user.user_name}.\n" + "\nMenu\n" + "-"*10 + "\n1. Add existing credentials \n" + "2. Create new credentials\n" + "3. View existing credentials\n" + "4. Logout")
                        print("\nPick an option:")
            
                        option = input()
            
                        if option == "1":
                            print("\n")
                            print("Enter the name of the account eg. Instagram")
                            enter_account_name = input()
                            print("Enter the account's username")
                            enter_account_username = input()
                            print("Enter the account's password")
                            enter_account_password = input()
                            
                            credentials = Credentials(enter_account_name, enter_account_username, enter_account_password)

                            add_existing_credentials(current_user, credentials)
        
                            print("\n" + f"{enter_account_name} saved successfully!")
        
                        elif option == "2":
                            pass
        
                        elif option == "3":
                            print("\n")
                            print("Saved accounts and passwords\n" + "-"*25)
                            
                            if list_credentials(current_user) == []:
                                print("No accounts have been saved.")
                            else:
                                for credential in list_credentials(current_user):
                                    print (credential.account_name + " " + "."*10 + " Username: " +         credential.user_name + " | " + "Password: " + credential.password)
        
                        elif option == "4":
                            break
                break

        elif option == "3":
            print("\nExisting Users\n" + "-"*20 + "\n")
            for username in User.list_users():
                print(username)
        
        elif option == "4":
            print("Goodbye.")
            break

        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
