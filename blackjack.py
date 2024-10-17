from blackjack_helper import *

num_players = int(input("How many players? "))

players = [input(f"Enter player {i+1}'s name: ") for i in range(num_players)] # players name stored in a list
scores = {player: 3 for player in players}  # Three score points for each player

# Loop of the game till the game ends or break statement is executed
while True:
        # Play a round for each player
        for player in players[:]:
            hand_value = draw_starting_hand(player)
            while hand_value < 21:
                should_hit = input(f"{player}, you have {hand_value}. Hit (y/n)? ").strip().lower()
                if should_hit == 'n':
                    break
                elif should_hit == 'y':
                    hand_value += draw_card()
                else:
                    print("Sorry, I didn't get that.")
            print_end_turn_status(hand_value)


        # Case for the dealer 
        dealer_hand = draw_starting_hand("DEALER")
        # Dealer to hit if the hand is less than 17
        while dealer_hand < 17:
            print(f"Dealer has {dealer_hand}.")
            dealer_hand += draw_card()
        print_end_turn_status(dealer_hand)
    
        # Compare each player's hand with dealer's hand and update scores
        for player in players[:]:
            print_end_game_status(player, hand_value, dealer_hand, scores)
            if scores[player] == 0:
                print(f"{player} eliminated!")
                players.remove(player)

        if not players:
            print("All players eliminated!")
            break

        # Ask if they want to play another round
        another_round = input("Do you want to play another hand (y/n)? ").strip().lower()
    
        if another_round != 'y': #Breaks if the player doesn't want to play another round
            break
