class Token:
    def __init__(self, token):
        self.token = token
        self.expired = False
        self.revoked = False
