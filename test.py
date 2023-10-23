import pytest
from server import application, games
from model.game import State

def get_client():
    application.run(host='0.0.0.0', debug = True, port = 80)
    return application.test_client()

def test_basic_win_scenario():
    player_id = 1
    dealer_id = 2
    client = get_client()
    response = client.get(f'''/start?player={player_id}&dealer={dealer_id}''')
    assert response.status_code == 200
    assert response.state == State.BET
    assert response.id
    assert response.deck
    assert len(response.deck) == 52
    assert response.bank == 0
    assert response.dealer
    assert response.player
    assert response.dealer.cards
    assert response.player.cards
    response = client.put(f'''/bet?id={response.id}&amount={100}''')
    assert response.bank == 100
    response = client.get(f'''/begin?id={response.id}''')
    assert response.state == State.DEAL
    assert len(response.player.cards) == 2

    # mocking cards on server
    games[response.id].player.cards = [(14, 1), (12, 3)] 
    games[response.id].dealer.cards = [(7, 1), (10, 1)]
    
    response = client.get(f'''/enough?id={response.id}''')
    assert response.state == State.RES
    assert response.winner == response.player


def test_basic_lose_scenario():
    player_id = 1
    dealer_id = 2
    client = get_client()
    response = client.get(f'''/start?player={player_id}&dealer={dealer_id}''')
    assert response.status_code == 200
    assert response.state == State.BET
    assert response.id
    assert response.deck
    assert len(response.deck) == 52
    assert response.bank == 0
    assert response.dealer
    assert response.player
    assert response.dealer.cards
    assert response.player.cards
    response = client.put(f'''/bet?id={response.id}&amount={100}''')
    assert response.bank == 100
    response = client.get(f'''/begin?id={response.id}''')
    assert response.state == State.DEAL
    assert len(response.player.cards) == 2

    # mocking cards on server
    games[response.id].dealer.cards = [(14, 1), (12, 4)] 
    games[response.id].player.cards = [(7, 1), (10, 1)]
    
    response = client.get(f'''/enough?id={response.id}''')
    assert response.state == State.RES
    assert response.winner == response.dealer

def test_fail_scenario():
    client = get_client()
    response = client.get('/start')
    assert response.status_code == 200
    response = client.get(f'''/begin?id={response.id}''')
    assert response.status_code >= 400

