# -*- coding: utf-8 -*-

import logging, time
from flask import Flask, app
from model.game import Game
from db import login_user, token_info, balance
from entity import user, token as tkn
import utils


application = Flask(__name__)
application.secret_key = 'jackovich'
log = logging.getLogger(__name__)
logging.basicConfig(level = logging.DEBUG, format = "> %(asctime)-15s %(levelname)-8s || %(message)s")

games = dict()
games_cnt = 0
id_cnt = 0

def generate_id():
    res = str(games_cnt)
    games_cnt += 1
    return res

@application.route('/start')
def start(player_id, dealer_id):
    game_id = generate_id()
    games[game_id] = Game(game_id, player_id, dealer_id)
    # TODO: serialize
    return games[game_id]

@application.route('/begin')
def begin(id):
    if games[id].bank <= 0: 
        return 'wrong bank', 400
    games[id].begin()
    return games[id]

@application.route('/bet')
def bet(id, user_id, amount):
    if (amount <= 0):
        return 'wrong bet', 400
    balance_ = balance.user_balance[user_id]
    if (balance_ < amount):
        return 'not enough money', 400
    balance_ -= amount
    games[id].make_bet(amount)
    return games[id]

@application.route('/enough')
def enough(id):
    games[id].enough()
    return games[id]

@application.route('/register')
def register(login, password):
    if (login in login_user):
        return 'already exists', 200
    hashed_password = hash.hash_password(password)
    login_user[login] = user.User(login, id_cnt, hashed_password)
    id_cnt += 1
    return 'registered', 200

@application.route('/login')
def login(login, password):
    if (not login in login_user):
        return 'no such user', 404
    hashed_password = hash.hash_password(password)
    user = login_user[login]
    if (hashed_password != user.hashed_password):
        return 'wrong password', 403
    token = utils.token.generate_token(login, user.id)
    token_info[token] = tkn.Token(token)
    balance.user_balance[user.id] = 777
    return token, 200

@application.route('/logout')
def logout(token):
    token_info[token].revoked = True

def main():
    application.run(host='0.0.0.0', debug = True, port = 80)

if __name__ == "__main__":
    main()
