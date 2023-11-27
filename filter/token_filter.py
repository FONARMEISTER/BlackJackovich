from db.token_info import token_info
import utils

def token_filter(token):
    if (not token in token_info):
        return 'registration expired', 400
    user_info = utils.extract_from_token(token)
    return user_info['login'], user_info['id']
