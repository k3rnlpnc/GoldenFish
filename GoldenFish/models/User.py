class User:
    def __init__(self, _email, _password, _username, _name, _surname, _dob):
        self.email = _email
        self.password = _password
        self.username = _username
        self.name = _name
        self.surname = _surname
        self.date_of_birth = _dob

    def get_id(self):  # id <- autoincrement
        pass

    def get_email(self):
        pass

    def set_email(self, email):
        pass
