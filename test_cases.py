import copy

from player import Player

game_state_mock = {
    "tournament_id": "550d1d68cd7bd10003000003",
    "game_id": "550da1cb2d909006e90004b1",
    "round": 0,
    "bet_index": 0,
    "small_blind": 10,
    "current_buy_in": 100,
    "pot": 400,
    "minimum_raise": 10,
    "dealer": 1,
    "orbits": 7,
    "in_action": 1,
    "players": [
        {
            "id": 0,
            "name": "Albert",
            "status": "active",
            "version": "Default random player",
            "stack": 1010,
            "bet": 320
        },
        {
            "id": 1,
            "name": "Bob",
            "status": "active",
            "version": "Default random player",
            "stack": 1590,
            "bet": 80,
            "hole_cards": [
                {
                    "rank": "6",
                    "suit": "clubs"
                },
                {
                    "rank": "K",
                    "suit": "clubs"
                }
            ]
        },
        {
            "id": 2,
            "name": "Chuck",
            "status": "out",
            "version": "Default random player",
            "stack": 0,
            "bet": 0
        }
    ],
    "community_cards": [
        {
            "rank": "4",
            "suit": "dsds"
        },
        {
            "rank": "3",
            "suit": "sds"
        },
        {
            "rank": "2",
            "suit": "clubs"
        }
    ]
}


def test_has_one_match():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "6",
            "suit": "clubs"
        },
        {
            "rank": "K",
            "suit": "hearts"
        }
    ]
    request['community_cards'] = [
        {
            "rank": "K",
            "suit": "spades"
        },
        {
            "rank": "3",
            "suit": "sdsd"
        },
        {
            "rank": "2",
            "suit": "clubs"
        }
    ]
    player = Player()
    res = player.betRequest(request)
    assert res == 20

def test_has_duplicates():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "6",
            "suit": "clubs"
        },
        {
            "rank": "6",
            "suit": "spades"
        }
    ]
    request['community_cards'] = [
        {
            "rank": "K",
            "suit": "hearts"
        },
        {
            "rank": "3",
            "suit": "spades"
        },
        {
            "rank": "2",
            "suit": "clubs"
        }
    ]
    player = Player()
    res = player.betRequest(request)
    print(res)
    assert res == 30

def test_has_double_match():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "6",
            "suit": "clubs"
        },
        {
            "rank": "K",
            "suit": "clubs"
        }
    ]
    request['community_cards'] = [
        {
            "rank": "K",
            "suit": "hearts"
        },
        {
            "rank": "6",
            "suit": "spades"
        },
        {
            "rank": "2",
            "suit": "clubs"
        }
    ]
    player = Player()
    res = player.betRequest(request)
    assert res == 60

def test_has_3_match():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "6",
            "suit": "clubs"
        },
        {
            "rank": "K",
            "suit": "hearts"
        }
    ]
    request['community_cards'] = [
        {
            "rank": "K",
            "suit": "hearts"
        },
        {
            "rank": "7",
            "suit": "spades"
        },
        {
            "rank": "K",
            "suit": "clubs"
        }
    ]
    player = Player()
    res = player.betRequest(request)
    print(res)
    assert res == 90

def test_has_straight():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "6",
            "suit": "clubs"
        },
        {
            "rank": "7",
            "suit": "clubs"
        }
    ]
    request['community_cards'] = [
        {
            "rank": "8",
            "suit": "hearts"
        },
        {
            "rank": "9",
            "suit": "hearts"
        },
        {
            "rank": "10",
            "suit": "spades"
        }
    ]
    player = Player()
    res = player.betRequest(request)
    assert res == 120

def test_has_flush():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "6",
            "suit": "clubs"
        },
        {
            "rank": "K",
            "suit": "clubs"
        }
    ]
    request['community_cards'] = [
        {
            "rank": "8",
            "suit": "clubs"
        },
        {
            "rank": "9",
            "suit": "clubs"
        },
        {
            "rank": "4",
            "suit": "clubs"
        }
    ]
    player = Player()
    res = player.betRequest(request)
    assert res == 180


def test_pay_for_community_cards():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "J",
            "suit": "clubs"
        },
        {
            "rank": "3",
            "suit": "clubs"
        }
    ]
    request['community_cards'] = []
    player = Player()
    res = player.betRequest(request)
    assert res == 20


def test_pay_for_community_cards_suits():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "5",
            "suit": "clubs"
        },
        {
            "rank": "3",
            "suit": "clubs"
        }
    ]
    request['community_cards'] = []
    player = Player()
    res = player.betRequest(request)
    assert res == 20


def test_has_full_house():
    request = copy.deepcopy(game_state_mock)
    request['players'][1]["hole_cards"] = [
        {
            "rank": "A",
            "suit": "clubs"
        },
        {
            "rank": "A",
            "suit": "clubs"
        }
    ]
    request['community_cards'] = [
        {
            "rank": "8",
            "suit": "hearts"
        },
        {
            "rank": "8",
            "suit": "hearts"
        },
        {
            "rank": "8",
            "suit": "hearts"
        }
    ]
    player = Player()
    res = player.betRequest(request)
    assert res == 210


def test_has_straight_unit():
    player = Player()
    assert player.has_straight(["2", "3"], ["5", "6", "7"]) is False
    assert player.has_straight(["2", "3"], ["4", "5", "6", "7"]) is True
    assert player.has_straight(["7", "9"], ["A", "6", "8", "Q", "10"]) is True
    assert player.has_straight(["A", "3"], ["A", "2", "5", "4"]) is True
    assert player.has_straight(["K", "A"], ["2", "3", "4"]) is False


def test_has_3_match_unit():
    player = Player()
    assert player.has_3_match(["2", "3"], ["A", "K", "3", "2", "3"]) is True
    assert player.has_3_match(["3", "3"], ["A", "K", "3", "2", "2"]) is True
    assert player.has_3_match(["3", "3"], ["A", "K", "2", "2", "2"]) is False


def test_has_4_match_unit():
    player = Player()
    assert player.has_4_match(["2", "3"], ["A", "K", "3", "3", "3"]) is True
    assert player.has_4_match(["3", "3"], ["3", "K", "3", "2", "2"]) is True
    assert player.has_4_match(["3", "3"], ["A", "K", "2", "2", "2"]) is False


test_has_one_match()
test_has_duplicates()
test_has_double_match()
test_has_3_match()
test_has_4_match_unit()
test_has_straight()
test_has_flush()
test_has_full_house()
test_pay_for_community_cards()
test_pay_for_community_cards_suits()
