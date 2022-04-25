#!/usr/bin/env python3.9
import pyperclip
from passlock import User
from passlock import Credentials


def function():
    print(
        "               _      _                                                               "
    )
    print(
        "              | |    | |                                                              "
    )
    print(
        "              | |    | |   __    _      ___    __    _    _    __                     "
    )
    print(
        "              | |/  \| |  / __\ | |    / _ \  /  \  |  \/  |  / __\                   "
    )
    print(
        "              |   /\   | |  __  | |_  | |_   | || | |  \/  | |  __                    "
    )
    print(
        "              |_ /  \_ |  \__ / |___|  \___/  \__/  |_|  |_|  \___/                   "
    )
    print(
        "                                 _______                                              "
    )
    print(
        "                                |__   __|                                             "
    )
    print(
        "                                   | |    __                                          "
    )
    print(
        "                                   | |   /  \                                         "
    )
    print(
        "                                   | |  | || |                                        "
    )
    print(
        "                                   |_|   \__/                                         "
    )
    print(
        "               ___                        _                                           "
    )
    print(
        "              |  _ \                     | |                                          "
    )
    print(
        "              | |_) )  ____  ___   ___   | |      __     __     _   _   __     _  _   "
    )
    print(
        "              |  __/  / _  |/ __  / __   | |     /  \   / _ \  | |/ /  / __\  | |/ /  "
    )
    print(
        "              | |    / (_| |\__ \ \__ \  | |___ | || | | |_    |   \  |  __   |  _/   "
    )
    print(
        "              |_|    \_____| ___/  ___/  |_____| \__/   \___/  |_|\_\  \___/  |_|     "
    )


function()


def create_new_user(username, password):
    """
    Function to create a new user with a username and password
    """
    new_user = User(username, password)
    return new_user


def save_user(user):
    """
    Function to save a new user
    """
    user.save_user()


def display_user():
    """
    Function to display existing user
    """
    return User.display_user()


def login_user(username, password):
    """
    function to check if a user exist and then login the user in.
    """

    check_user = Credentials.verify_user(username, password)
    return check_user


def create_new_credential(account, userName, password):
    """
    Function to create new credentials for a user account
    """
    new_credential = Credentials(account, userName, password)
    return new_credential


def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_details()


def display_accounts_details():
    """
    Function to display all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()


def find_credential(account):
    """
    Function to find a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)


def check_credentials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)


def generate_Password():
    """
    function to generate a random password for the user.
    """
    auto_password = Credentials.generatePassword()
    return auto_password


def copy_password(account):
    """
    function to copy the password using the pyperclip
    """
    return Credentials.copy_password(account)


def passlocker():
    print(
        "Hello there Welcome to Password Locker...\n Please select one of the short codes below to proceed:\n NA ---  Create New Account  \n LG ---  LogIn  \n"
    )
    short_code = input("").lower().strip()
    if short_code == "na":
        print("Sign Up")
        print("*" * 50)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == "tp":
                password = input("Enter Password\n")
                break
            elif password_Choice == "gp":
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username, password))
        print("*" * 80)
        print(
            f"Hello {username}, Your account has been created succesfully! Your password is: {password}"
        )
        print("*" * 80)
    elif short_code == "lg":
        print("*" * 45)
        print("Enter your User name and your Password to log in:")
        print("*" * 45)
        username = input("Username: ")
        password = input("password: ")
        login = login_user(username, password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWord Locker")
            print("\n")
    while True:
        print(
            "Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n"
        )
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("." * 20)
            print("Account name :")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(
                    " TP - To type your own password if you already have an account:\n GP - To generate random Password"
                )
                password_Choice = input().lower().strip()
                if password_Choice == "tp":
                    password = input("Type your preffered password\n")
                    break
                elif password_Choice == "gp":
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account, userName, password))
            print("\n")
            print(
                f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully"
            )
            print("\n")
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acounts: ")

                print("*" * 30)
                print("_" * 30)
                for account in display_accounts_details():
                    print(
                        f" Account:{account.account} \n User Name:{username}\n Password:{password}"
                    )
                    print("_" * 30)
                print("*" * 30)
            else:
                print("No credentials found:(")
        elif short_code == "fc":
            print("Please enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print("-" * 50)
                print(
                    f"User Name: {search_credential.userName} Password :{search_credential.password}"
                )
                print("-" * 50)
            else:
                print("The Credential does not exist")
                print("\n")
        elif short_code == "del":
            print("Enter the account name for the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_" * 50)
                search_credential.delete_credentials()
                print("\n")
                print(
                    f"Your credentials for : {search_credential.account} has been deleted successfully"
                )
                print("\n")
            else:
                print(
                    "The Credentials you want to delete does not exist,please enter an existing account"
                )

        elif short_code == "gp":

            password = generate_Password()
            print(
                f" {password} Has been generated succesfull. Proceed to use it to your account"
            )
        elif short_code == "ex":
            print("Thanks for using passwords locker.. Have a nice day!")
            break
        else:
            print("Wrong entry... Check your entry and retry")
    else:
        print("Please enter a valid input to continue")


if __name__ == "__main__":
    passlocker()
