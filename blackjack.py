#!/usr/bin/python

import sys
import random

def shuffle():
    # TODO - generate a randomly permuted deck of cards using random.randrange()
    return []

def ante(player):
    # TODO - record the player's initial ante bet
    pass

def deal(deck, player_hand, dealer_hand):
    # TODO - deal initial hands to the player and dealer
    pass

def bet(player):
    # TODO - prompt the player for a bet and record it
    pass

def payoff(player):
    # TODO - record the payment of the player's winnings or losses fot this hand
    pass

def main():
    deck = shuffle()
    player = {
        'chips' : 100,
        'hand' : [],
    }

    print "Welcome to Blackjack"

    while player['chips'] > 0:
        print "You have ", player['chips'], " chips."
        ante(player)
        dealer_hand = []
        deal(deck, player['hand'], dealer_hand)
        bet(player)
        
        # TODO - play the hand

        payoff(player)
    return 0

if __name__ == '__main__':
    sys.exit(main())
