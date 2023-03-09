import p1_random as p1

def main():

    #defining variables inside main

    game_continue = True
    player_hand = 0
    menu = '1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n'
    dealer_wins = 0
    player_wins = 0
    game_num = 1
    tie_games = 0
    
    #creating an array that includes the names of the cards and their corresponding values

    cards = [['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING'],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]]
    
    rng = p1.P1Random()
    new_card = rng.next_int(13) + 1
    player_hand += cards[1][new_card - 1]

    print(f'START GAME #{game_num}\n')
    print('Your card is a '+cards[0][new_card - 1]+'!')
    print(f'Your hand is: {player_hand}\n')
    print(menu)
    #while loop so that the game will continue for as long as the player wants to play

    while game_continue:

    # takes an input from the player of the menu options

        menu_select = int(input('Choose an option: '))
        print()
    # end input

    # using a match case statement to more easily format how the program will
# progress when a menu selection is picked

        match menu_select:

            case 1:
        #creates a new value from p1.random and sets it equal to the player's hand

                new_card = rng.next_int(13) + 1

        #adds the new card value to the player's hand

                player_hand += cards[1][new_card - 1]

                if player_hand > 21:
                    print('Your card is a '+cards[0][new_card - 1]+'!')
                    print(f'Your hand is: {player_hand}\n')
                    win(False,True,False,False,False)
                    dealer_wins += 1
                    player_hand = 0
                    game_num += 1
                    print(f'START GAME #{game_num}\n')
                    player_hand += cards[1][new_card - 1]
            

            case 2:
                
                dealer_hand = rng.next_int(11) + 16

                print('Dealer\'s hand:', dealer_hand)
                print(f'Your hand is: {player_hand}\n')
                
                if dealer_hand > 21:
                    player_wins += win(True,False,False,False,False)

                elif player_hand > dealer_hand and player_hand <= 21:
                    player_wins += win(True,False,False,False,False)

                elif player_hand < dealer_hand and dealer_hand <= 21:
                    dealer_wins += win(False,False,True,False,False)

                elif player_hand == dealer_hand:
                    tie_games += win(False,False,False,True,False)

                player_hand = 0

                game_num += 1

                print(f'START GAME #{game_num}\n')

                player_hand += cards[1][new_card - 1]


            
                
            case 3:
                print(f'Number of Player wins: {player_wins}')
                print(f'Number of Dealer wins: {dealer_wins}')
                print(f'Number of tie games: {tie_games}')
                print(f'Total # of games played is: {game_num}')
                print(f'Percentage of Player wins: {player_wins / game_num}%\n')
                print(menu)
        
                
            case 4:
                exit()
                
            case _:
                print('Invalid input!\nPlease enter an integer value between 1 and 4.\n')
                print(menu)
            
        
#print hand start
                    
        print('Your card is a '+cards[0][new_card - 1]+'!')
        print(f'Your hand is: {player_hand}\n')

# end print hand

# this block of code is for checking bj start bj check


        if player_hand == 21:
            win(False,False,False,False,True)
            player_wins += 1
            player_hand = 0
            game_num += 1
            print(f'START GAME #{game_num}\n')
            continue

# end bj check

        print(menu)

#defining a global win variable in order to make the case arguments less lengthy

def win(player:bool, bust:bool, dealer:bool, tie:bool, blackjack:bool):
    
    if player == True and bust == False and dealer == False and tie == False and blackjack == False:
        print('You win!\n')

    elif player == False and bust == True and dealer == False and tie == False and blackjack == False:
        print('You exceeded 21! You lose.\n')
    
    elif player == False and bust == False and dealer == True and tie == False and blackjack == False:
        print('Dealer wins!\n')

    elif player == False and bust == False and dealer == False and tie == True and blackjack == False:
        print('It\'s a tie! No one wins!\n')
    
    elif player == False and bust == False and dealer == False and tie == False and blackjack == True:
        print('BLACKJACK! You win!\n')  

    return 1

main()

