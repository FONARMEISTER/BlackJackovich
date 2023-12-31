import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

def check_password(password, hashed_password):
    return bcrypt.checkpw(password, hashed_password)
