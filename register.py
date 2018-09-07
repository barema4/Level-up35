class Registration:
    def __init__ (self):
        self.data=dict()

    def add(self, firstname, lastname):
        self.data[firstname] = lastname

    def get_lastname(self, firstname):
        return self.data[firstname]

    def add_credentials(self, username, password ):
        self.data[username] = username
        self.data[password] = password
        return self.data[username], self.data[password]

    def add_address(self, email,telephone_number):
        self.data[email] = email
        self.data[telephone_number] = telephone_number
        return self.data[email], self.data[telephone_number]

    

    
