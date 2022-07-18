class User:
    def __init__(username: str, password: str):
        self.username = username
        self.password = password
        self.is_logged_in = False
        
    def login(self, inp_username: str, inp_password: str):
        if inp_username == self.username and inp_password == self.password:
            self.is_logged_in = True
            return True
        else:
            return False