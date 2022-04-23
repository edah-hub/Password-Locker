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
        User.user_list.append(self)
    