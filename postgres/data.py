
import time
import psycopg2

class DatabaseConnection():
    def event(self):
        

        try:

        
            self.connection = psycopg2.connect(dbname='levelup35',
                                                   user='postgres',
                                                   password='Get/2014',
                                                   host='localhost',
                                                   port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('\n\nConnected to Database\n\n')
                
        except(Exception, psycopg2.DatabaseError) as error:
            raise error
            user = DatabaseConnection()

            user.event()

def insert_user(self, first_name,last_name,email, password,sex):
        
        self.cursor.execute("SELECT * FROM Users WHERE email = %s", [email])
        check_email = self.cursor.fetchone()
    
        if check_email:
            return "email exits friend"

        insert_item = "INSERT INTO Users(first_name,last_name, email, password,sex) VALUES('"+first_name+"', '"+last_name+"', '"+email+"', '"+password+"'+'"+sex+"')"
        self.cursor.execute(insert_item)
        return "you have successfully created an account"

def all_users(self):
        
        user = "SELECT * FROM Users"
        self.cursor.execute(user)
        keys = ["first_name", "last_name", "email", "age","password","created_at"]
        Users = self.cursor.fetchall(),
        user_list = []
        for user in Users:
            user_list.append(dict(zip(keys, user)))
        if not user_list:
            return "No one"

        return user_list

def delete_user(self, user_id):
        
        self.cursor.execute("SELECT * FROM Users WHERE user_id = %s", [user_id])
        check_user_id = self.cursor.fetchone()
        if not check_user_id:
            return "user doesnot exist"


        self.cursor.execute("SELECT * FROM Users WHERE user_id = %s", [user_id])
        check_user_id = self.cursor.fetchone()
        if not check_user_id:
            return "user deleted"

        
