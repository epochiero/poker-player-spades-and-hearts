import random
from collections import Counter
from itertools import filterfalse


class Player:
    VERSION = "1.2"

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
        community_cards = game_state['community_cards']

        my_cards_ranks = [c['rank'] for c in my_cards]
        my_cards_suits = [c['suit'] for c in my_cards]

        community_cards_ranks = [c['rank'] for c in community_cards]
        community_cards_suits = [c['suit'] for c in community_cards]

        all_card_suits = my_cards_suits + community_cards_suits
        my_cards_suits_matches_community = self.has_common_elements(my_cards_ranks, community_cards_suits)
        suits_count = self.count_elements(all_card_suits)

        call_bet = current_buy_in - my_bet # call
        raise_bet = current_buy_in - my_bet + minimum_raise # raise

        # if not community_cards and self.pay_for_community_cards(my_cards):
        #     print("pay for community cards")

        if self.has_flush(all_card_suits):
            print("flush")
            return raise_bet * 5

        if self.has_straight(my_cards_ranks, community_cards_ranks):
            print("straight")
            return raise_bet * 4

        if self.has_3_match(my_cards_ranks, community_cards_ranks):
            print("3 match")
            return raise_bet * 3

        if self.has_double_match(my_cards_ranks, community_cards_ranks):
            print("double")
            return raise_bet * 2

        if self.has_duplicates(my_cards_ranks):
            print("duplicates")
            return raise_bet

        if self.has_one_match(my_cards_ranks, community_cards_ranks):
            print("one match")
            return call_bet

        print("fold")
        return 0

    def has_duplicates(self, array):
        return len(array) != len(set(array))

    def has_common_elements(self, arr1, arr2):
        return not set(arr1).isdisjoint(arr2)

    def has_one_match(self, my_card, community_card):
        return len(set(my_card) & set(community_card)) == 1

    def has_double_match(self, my_card, community_card):
        return len(set(my_card) & set(community_card)) == 2

    def has_3_match(self, my_card, community_card):
        element_counts = Counter(my_card+community_card)
        values_with_three = [key for key, count in element_counts.items() if count == 3]
        return self.has_one_match(my_card, values_with_three)


    def has_straight(self, my_card, community_card):
        all_cards = my_card + community_card
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
        }

        values = sorted(card_values[card] for card in all_cards)

        # Check for duplicates
        if len(values) != len(set(values)):
            return False

        # Check for consecutive values
        return values[-1] - values[0] == 4 and len(values) == 5

    def has_flush(self, all_cards):
        element_counts = self.count_elements(all_cards)
        for elem in element_counts:
            if element_counts[elem] >= 5 and (all_cards[0] == elem or all_cards[1] == elem):
                return True

    def count_elements(self, arr):
        # Using Counter to count the occurrences of each element in the array
        return dict(Counter(arr))

    # def pay_for_community_cards(self, my_cards):
    #     first_card_match = self.has_one_match([my_cards[0]], ['J', 'Q', 'K', 'A'])
    #     second_card_match = self.has_one_match([my_cards[1]], ['J', 'Q', 'K', 'A'])
    #
    #     return first_card_match and second_card_match