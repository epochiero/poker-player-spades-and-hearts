from random import sample
from itertools import product
from pokerlib import HandParser
from pokerlib.enums import Rank, Suit


suit = {
    'spades': Suit.SPADE,
    'clubs': Suit.CLUB,
    'diamonds': Suit.DIAMOND,
    'hearts': Suit.HEART
}

rank = {
    '2': Rank.TWO,
    '3': Rank.THREE,
    '4': Rank.FOUR,
    '5': Rank.FIVE,
    '6': Rank.SIX,
    '7': Rank.SEVEN,
    '8': Rank.EIGHT,
    '9': Rank.NINE,
    '10': Rank.TEN,
    'J': Rank.JACK,
    'Q': Rank.QUEEN,
    'K': Rank.KING,
    'A': Rank.ACE
}


def winning_probability(player_cards, board=None, n=1000, num_other_players=3):
    if board is None:
        board = []
    player_cards = [(rank[card[0]], suit[card[1]]) for card in player_cards]
    board = [(rank[card[0]], suit[card[1]]) for card in board]
    cards = list(product(Rank, Suit))
    for card in board:
        cards.remove(card)
    for card in player_cards:
        cards.remove(card)

    other_players = []
    for i in range(num_other_players):
        other_player_cards = sample(cards, 2)
        other_players.append(other_player_cards)
        for card in other_player_cards:
            cards.remove(card)

    wins = [0] * (num_other_players + 1)
    for i in range(n):
        board_ = sample(cards, 5 - len(board))
        hands = [
            HandParser(player + board + board_) for player in [player_cards] + other_players
        ]
        winner = max(hands)
        for i, hand in enumerate(hands):
            if hand == winner:
                wins[i] += 1

    return [win / n for win in wins]


winning_probability([['K', 'spades'], ['K', 'hearts']])
