class User:

    """

    Class that generates new instances of user login into my aplication.

    """

    user_list = []

    def __init__(self,first_name,last_name,email,password):

        """
        Define properties for my object.

        """

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_user(self):

        '''
        method to save user.
        '''

        User.user_list.append(self)

    def delete_user(self):
        
        '''
        method to delete a saved user.
        '''
        User.user_list.remove(self)