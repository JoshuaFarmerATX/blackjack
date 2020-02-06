import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        return

    def show(self):
        return f'{self.val} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for i in ['Hearts', 'Clubs', 'Spades', 'Diamonds']:
            for n in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
                self.cards.append(Card(i, n))
        random.shuffle(self.cards)
    
    def show(self):
        return [i.show() for i in self.cards]

class Deal:
    def __init__(self, deck, hand = []):
        self.deck = deck
        self.hand = hand

    def deal(self):
        hand = self.deck[0:2]
        del self.deck[0:2]
        return hand
    
    def hit(self):
        hand.append(self.deck[0])
        del self.deck[0]
        return hand

class Score:
    def __init__(self, hand_cards):
        self.hand_cards = hand_cards

    def score_hand(self):
        n = self.hand_cards[:]
        for i in range(0, len(n)):
            if isinstance(n[i], int):
                n[i] = n[i]
            elif '2' in n[i]:
                n[i] = 2
            elif '3' in n[i]:
                n[i] = 3
            elif '4' in n[i]:
                n[i] = 4
            elif '5' in n[i]:
                n[i] = 5
            elif '6' in n[i]:
                n[i] = 6
            elif '7' in n[i]:
                n[i] = 7
            elif '8' in n[i]:
                n[i] = 8
            elif '9' in n[i]:
                n[i] = 9
            elif 'Ace' in n[i]:
                n[i] = 11
            elif 'King' in n[i]:
                n[i] = 10
            elif 'Queen' in n[i]:
                n[i] = 10
            elif 'Jack' in n[i]:
                n[i] = 10
            elif '10' in n[i]:
                n[i] = 10
            
        for i in range(0, len(n)):
            if n[i] == 11:
                if sum(n) > 21:
                    n[i] = 1
        return n

class Player():
    def __intit__(self, full_deck = None, hand = None):
        if full_deck is None:
            full_deck = []
        self.full_deck = full_deck
        if hand is None:
            hand = []
        self.hand = hand

    def new_game(self):
        self.full_deck = Deck().show()
        return self.full_deck

    def deal(self):
        hand = Deal(deck).deal()
        return hand

    def hit(self):
        Deal(deck, hand).hit()
        return hand


class Dealer(Player):
    def hit(self):
        while sum(Score(hand).score_hand()) < 17:
            Deal(deck, hand).hit()
        print("The dealer's hand is...")
        for i in hand:
            print(i)


player_choice = 0
while player_choice != 5:
    player_choice = int(input('''
    What would you like to do?
    1. New Game
    2. Deal
    3. Hit
    4. Call
    5. Exit'''
    ))
    if player_choice == 1:
        deck = Player().new_game()
        print('We are shuffled up! lets play')
    if player_choice == 2:
        if len(deck) < 4:
            deck = Player().new_game()
            print('Reshuffling...')
        hand = Player().deal()
        print('Your hand is...')
        for i in hand:
            print(i)
        print(f'Your score is {sum(Score(hand).score_hand())}')
        dealer_hand = Dealer().deal()
        print(f'Dealer is showing a {dealer_hand[0]}')
    if player_choice == 3:
        if len(deck) < 1:
            deck = Player().new_game()
            print('Reshuffling...')
        hand = Player().hit()
        print('Your hand is...')
        for i in hand:
            print(i)
        if sum(Score(hand).score_hand()) < 22:
            print(f'Your score is {sum(Score(hand).score_hand())}')
        else:
            print(f'Your score is {sum(Score(hand).score_hand())}')
            print('Ya Busted!')
            player_choice = 6
    if player_choice == 4:
        print(f'Your score is {sum(Score(hand).score_hand())}')
        player_hand = hand
        hand = dealer_hand
        print("Dealer's Turn!")
        Dealer().hit()
        print(f'Dealer score is {sum(Score(hand).score_hand())}')
        if (sum(Score(hand).score_hand()) >= sum(Score(player_hand).score_hand())) and (sum(Score(hand).score_hand()) <= 21):
            print('Dealer Wins')
        else:
            print('You win!')
        player_choice = 6
    if player_choice == 6:
        print('Would you like to try again?')
        play_again = int(input('''
        1. Yes
        2. no'''))
        if play_again == 2:
            player_choice = 5
