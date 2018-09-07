class GuestList:
    def __init__(self):        
        self.users=[]

    def get_all_users(self):
        return self.users

    def add_user(self,first_name,last_name,email,password):
        xl = [user for user in self.users]

        user_id = len(xl)+1
        
        user={
            'firstName':first_name, 'lastName':last_name, 'email':email,'pin':password,
            'user_id':user_id
        }
        self.users.append(user)
        return self.users
    
    def remove_user(self,user_id):        
        for user in self.users:
            if user['user_id'] == user_id:
                self.users.remove(user)
        return "Not found"