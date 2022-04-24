from requests import delete
import random
import string
import pyperclip


class User:
    '''
    class that generates an instance of User
    '''
    user_list = []
    
    def __init__(self, username, password):
        '''
        method that defines the properties of user
        '''
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        A method that saves a new user instance into the user list
        '''
        User.user_list.append(self)  # Appending / adding new password by appending to out user_list[]
    
    # def display_user(self):
    @classmethod
    def display_user(cls):
        return cls.user_list
    
    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self) # Using the remove() method to delete the user object from the user_list.
    
class Credentials():
    '''
    Create credentials class to help create new objects of credentials
    ''' 
    credentials_list = []
    @classmethod
    def verify_user(cls,username,password):
        '''
        method to verify whether the user is in the user_list
        '''  
        x_user = ""
        for user in User.user_list:
            if (user.username == username and user.password == password):
                x_user == user.username
        return x_user  
    
    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password 
        
    def save_details(self):
        '''
        method to save new credentials to the credential lst
        '''
        Credentials.credentials_list.append(self) # Appending / adding new password by appending to out user_list[]
        
    def delete_details(self):
        '''
        method to delete existing credentials
        '''
        Credentials.credentials_list.remove(self)  # Using the remove() method to delete the user object from the user_list.
        
    @classmethod
    def find_credential(cls, account):
        '''
        method that takes the account_name and return credentials that matches the account
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
        
    @classmethod
    def copy_password(cls,account):
        '''
        method that takes allows copying and pasting a credential
        '''
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password) #pyperclip.copy() method allows us to copy passed in items to the machines clipboard
        
    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        '''
        Method that returns all items in the credentials list

        '''
        return cls.credentials_list
    
    def generatePassword(stringLength=8):
        '''
        Generate a random password string of letters and digits and special characters
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))