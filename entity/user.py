class User:

    def __init__(self, login, id, password):
        self.id = id
        self.is_auth = False
        self.login = login
        self.hashed_password = password
