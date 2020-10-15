# PassLock
#### Vault that stores passwords to accounts and generates passwords for new accounts
#### By **Victor Maina**
## Description
PassLock is a simple Python app that stores users' passwords. Using the CLI, a user can create a new account to store passwords to existing accounts. They can also create new accounts, and choose whether to generate a new password or not. The user navigated the app using number codes, an idea inpired by mobile USSD technology. This makes navigation easier, as opposed to using shortcodes.

## Setup/Installation Requirements

To use the app, you need to run it locally on a terminal. Use Git to clone this repository.
```
$ git clone https://github.com/VictorKMaina/password-vault.git
```

The app requires Python to run. To install Python on Ubuntu, do this:
```
$ sudo apt install python3.9
```

Once this is done, navigate in the `password-vault` directory and run the app.
```
$ ./run.py
```

## Navigating the app
Upon running the app, this is what you will see:
```
Welcome to PassLocker.

1. Create New Account
2. Log In
3. Show existing users
4. Exit PassLocker

Choose an option:
```

To create a new account, enter `1`.

All the navigation in the app is done in similar format, as directed by its instructions.

## Known Bugs
Currently, a user cannot delete an account once they've have added. This will be resolved in later development.


## Support and contact details
If you have any issues, questions, or ideas concerning the app, you can [email me](mailto:contact@victormaina.com).

## [LICENSE](./LICENSE)
