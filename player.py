import random


class Player:
    VERSION = "0.3"

    def showdown(self, game_state):
        return ""

    def betRequest(self, game_state):
        # To raise, the player has to return an amount larger than current_buy_in - players[in_action][bet] + minimum_raise.
        # This is the amount necessary to call plus the smallest valid raise.
        # Smaller bets are either treated as call or fold depending on the amount.
        # To call the player needs to return current_buy_in - players[in_action][bet], that is the largest bet from
        # any of the players minus the bet already made by the current player.
        # Any bet smaller than this amount is treated as a fold.

        current_buy_in = game_state['current_buy_in']  # current max bet
        minimum_raise = game_state['minimum_raise']  # current min raise
        my_player = game_state['players'][game_state['in_action']]
        my_cards = my_player['hole_cards']

        my_bet = my_player['bet']  # my current bet
        my_money = my_player['stack']
        my_cards = my_player['hole_cards']
        my_cards_ranks = [c['rank'] for c in my_player['hole_cards']]
        # community_cards = game_state['community_cards']

        if self.has_duplicates(my_cards_ranks):
            return current_buy_in - my_bet # call
        else:
            return 0


        # if random.randint(0, 1) == 1:
        #     # Raise
        #     return current_buy_in - my_bet + minimum_raise
        # else:
        #     # Call
        #     return current_buy_in - my_bet

    def has_duplicates(self, array):
        return len(array) != len(set(array))