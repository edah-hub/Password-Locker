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
        User.user_list.remove(self) # Using the remove() method to delete the contact object from the user_list.
    
class Credentials():
    '''
    Create credentials class to help create new objects of credentials
    '''       