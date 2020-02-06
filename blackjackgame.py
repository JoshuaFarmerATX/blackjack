from blackjack import *

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
        hand = Player().deal()
        print('Your hand is...')
        for i in hand:
            print(i)
        print(f'Your score is {sum(Score(hand).score_hand())}')
        dealer_hand = Dealer().deal()
        print(f'Dealer is showing a {dealer_hand[0]}')
    if player_choice == 3:
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
