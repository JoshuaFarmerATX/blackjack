import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        return

    def show(self):
        return f"{self.val} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ["Hearts", "Clubs", "Spades", "Diamonds"]:
            for n in [
                "Ace",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "Jack",
                "Queen",
                "King",
            ]:
                self.cards.append(Card(i, n))
        random.shuffle(self.cards)

    def show(self):
        return [i.show() for i in self.cards]


class Deal:
    def __init__(self, deck, hand=[]):
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
        for i in range(len(n)):
            if isinstance(n[i], str):
                try:
                    if int(n[i][0:2]) == 10:
                        n[i] = 10
                    elif isinstance(int(n[i][0]), int):
                        n[i] = int(n[i][0])
                except:
                    if n[i][0] == "K" or n[i][0] == "Q" or n[i][0] == "J":
                        n[i] = 10
                    else:
                        n[i] = 11
            else:
                pass

        for i in range(0, len(n)):
            if n[i] == 11:
                if sum(n) > 21:
                    n[i] = 1

        return n


class Player:
    def __intit__(self, full_deck=None, hand=None):
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
while player_choice != 2:
    try:
        player_choice = int(
            input(
                """
      BLACKJACK
 ________    ________   
|A       |  |J       |
|   /\   |  |   /\   |
|   \/   |  |   \/   |
|_______A|  |_______J|

What would you like to do? Numerical input only!
    1. New Game
    2. Exit
    """
            )
        )
        if player_choice == 1:
            deck = Player().new_game()
            print("We are shuffled up! lets play")
            play_menu = 0
            while play_menu != 4:
                play_menu = int(
                    input(
                        """
    1. Deal new hand
    2. Hit
    3. Call
    4. Exit to main menu
    """
                    )
                )
                if play_menu == 1:
                    if len(deck) < 4:
                        deck = Player().new_game()
                        print("Reshuffling...")
                    hand = Player().deal()
                    print("Your hand is...")
                    for i in hand:
                        print(i)
                    print(f"Your score is {sum(Score(hand).score_hand())}")
                    dealer_hand = Dealer().deal()
                    print(f"Dealer is showing a {dealer_hand[0]}")
                elif play_menu == 2:
                    if len(deck) < 1:
                        deck = Player().new_game()
                        print("Reshuffling...")
                    if len(hand) < 2:
                        print("you have to deal before you can hit")
                    else:
                        hand = Player().hit()
                        print("Your hand is...")
                        for i in hand:
                            print(i)
                        if sum(Score(hand).score_hand()) < 22:
                            print(f"Your score is {sum(Score(hand).score_hand())}")
                        else:
                            print(f"Your score is {sum(Score(hand).score_hand())}")
                            print("Ya Busted!")
                            play_menu = 5
                elif play_menu == 3:
                    print(f"Your score is {sum(Score(hand).score_hand())}")
                    player_hand = hand
                    hand = dealer_hand
                    print("Dealer's Turn!")
                    Dealer().hit()
                    print(f"Dealer score is {sum(Score(hand).score_hand())}")
                    if (
                        sum(Score(hand).score_hand())
                        >= sum(Score(player_hand).score_hand())
                    ) and (sum(Score(hand).score_hand()) <= 21):
                        print("Dealer Wins")
                    else:
                        print("You win!")
                    play_menu = 5

                if play_menu == 5:
                    hand = []
                    print("Would you like to try again?")
                    play_again = int(
                        input(
                            """
    1. Yes
    2. no
    """
                        )
                    )
                    if play_again == 2:
                        player_choice = 0
                        play_menu = 4

                if play_menu > 5:
                    play_menu = "fourty two"
    except:
        print(
            """
What did you do!?!?! Type a letter instead of a number?
Did you try to hit or call before dealing your starting hand?
Did you write out a really long number like 42? It isn't always the answer you know!

Either way, you would lose 500 points if there were points in this game. For shame!

Back to the main menu to try again!
            """
        )
        player_choice = 0
