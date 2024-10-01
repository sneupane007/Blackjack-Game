from random import randint

def print_card_name(card_rank):
    
    if card_rank == 1:
    # A 1 stands for an ace.
        card_name = "Ace"
        
    elif card_rank == 11:
    # An 11 stands for a jack.
        card_name = "Jack"
        
    elif card_rank == 12:
    # A 12 stands for a queen.
        card_name = "Queen"
        
    elif card_rank == 13:
    # A 13 stands for a king.
        card_name = "King"
    else:
    # All other cards are named by their
    # number, or rank.
        card_name = str(card_rank)
    
    
    if card_rank == 1 or card_rank == 8:
        drew_prefix = 'Drew an '
    else:
        drew_prefix = 'Drew a '

    if card_rank<1 or card_rank>13:
        print("BAD CARD")
    else:
        print(drew_prefix + card_name)


def draw_card():
    
    card_rank = randint(1,13)
    print_card_name(card_rank) 
    if card_rank > 10:
        return 10
    elif card_rank == 1:
        return 11
    else:
        return card_rank 


def print_header(message):
    print("-----------")
    print(message.upper())
    print("-----------")
    
    
def draw_starting_hand(name):
    print_header(f"{name} TURN")
    card_1 = draw_card()
    card_2 = draw_card()

    return (card_1 + card_2)
    

def print_end_turn_status(hand_value):

    print("Final hand: " + str(hand_value)+".")
    if hand_value == 21:
        print("BLACKJACK!")
    elif hand_value >21:
        print("BUST.")


def print_end_game_status(user_hand, dealer_hand):
    
    print_header("GAME RESULT")
    
    if user_hand > 21:
        print("Dealer wins!")  # User busts
    elif dealer_hand > 21:
        print("You win!")  # Dealer busts
    elif user_hand > dealer_hand:
        print("You win!")  # User has a higher hand
    elif dealer_hand > user_hand:
        print("Dealer wins!")  # Dealer has a higher hand
    else:
        print("Push.")  # Both hands are equal
    