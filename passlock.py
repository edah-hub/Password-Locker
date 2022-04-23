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
    