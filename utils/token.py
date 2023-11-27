import jwt

SECRET = "WHITE_JACKOVICH"

def generate_token(login, id):
    return jwt.encode({"id": id, "login" : login}, SECRET, algorithm="SHA256")


def extract_from_token(token):
    return jwt.decode(token, SECRET, algorithms=["SHA256"])
