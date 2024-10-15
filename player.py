import random


class Player:
    VERSION = "1.0"

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
        community_cards = game_state['community_cards']
        community_cards_ranks = [c['rank'] for c in community_cards]

        call_bet = current_buy_in - my_bet # call
        raise_bet = current_buy_in - my_bet + minimum_raise # raise


        if self.has_double_match(my_cards_ranks, community_cards_ranks):
            return raise_bet * 2
        elif self.has_duplicates(my_cards_ranks):
            return raise_bet
        elif self.has_one_match(my_cards_ranks, community_cards_ranks):
            return call_bet
        else:
            return 0

    def has_duplicates(self, array):
        return len(array) != len(set(array))

    def has_common_elements(self, arr1, arr2):
        return not set(arr1).isdisjoint(arr2)

    def has_one_match(self, my_card, community_card):
        return len(set(my_card) & set(community_card)) == 1

    def has_double_match(self, my_card, community_card):
        return len(set(my_card) & set(community_card)) == 2
