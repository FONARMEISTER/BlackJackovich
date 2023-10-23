# -*- coding: utf-8 -*-

import logging
from flask import Flask, app
from model.game import Game

application = Flask(__name__)
application.secret_key = 'jackovich'
log = logging.getLogger(__name__)
logging.basicConfig(level = logging.DEBUG, format = "> %(asctime)-15s %(levelname)-8s || %(message)s")

games = dict()
games_cnt = 0

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
    games[id].begin()
    return games[id]

@application.route('/bet')
def bet(id, amount):
    games[id].make_bet(amount)
    return games[id]

@application.route('/enough')
def enough(id):
    games[id].enough()
    return games[id]

def main():
    application.run(host='0.0.0.0', debug = True, port = 80)

if __name__ == "__main__":
    main()
