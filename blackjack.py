import p1_random as p1

def main():

    game_continue = True
    player_hand = 0
    menu = '1.  Get another card\n2.  Hold hand\n3.  Print statistics\n4.  Exit\n'
    dealer_wins = 0
    player_wins = 0
    game_num = 1
    tie_games = 0
    
    cards = [['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING'],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]]
    
    rng = p1.P1Random()

    print(f'START GAME #{game_num}\n')

    while game_continue:

        new_card = rng.next_int(13) + 1

        player_hand += cards[1][new_card - 1]

        print('Your card is a '+cards[0][new_card - 1]+'!')
        print(f'Your hand is: {player_hand}\n')
        print(menu)

        menu_select = int(input('Choose an option: '))
        print()

        match menu_select:

            case 1:

                if player_hand > 21:
                    win(False,True,False,False)
                    dealer_wins += 1
                    player_hand = 0
                    game_num += 1
                    print(f'START GAME #{game_num}\n')
            
            case 2:
                
                dealer_hand = rng.next_int(11) + 16
                
                if dealer_hand > 21:
                    player_wins += win(True,False,False,False)

                elif player_hand > dealer_hand and player_hand <= 21:
                    player_wins += win(True,False,False,False)

                elif player_hand < dealer_hand and dealer_hand <= 21:
                    dealer_wins += win(False,False,True,False)

                elif player_hand == dealer_hand:
                    tie_games += win(False,False,False,True)

                player_hand = 0

                game_num += 1

                print(f'START GAME #{game_num}\n')
                
            case 3:
                print(f'Number of Player wins: {player_wins}')
                print(f'Number of Dealer wins: {dealer_wins}')
                print(f'Number of tie games: {tie_games}')
                print(f'Total # of games played is: {game_num}')
                print(f'Percentage of Player wins: {player_wins / game_num}%')
                print(menu)
                
            case 4:
                exit()
                
            case _:
                print('Invalid input!\nPlease enter an integer value between 1 and 4.')

def win(player:bool, bust:bool, dealer:bool, tie:bool):
    
    if player == True and bust == False and dealer == False and tie == False:
        print('You win!\n')

    elif player == False and bust == True and dealer == False and tie == False:
        print('You exceeded 21! You lose.\n')
    
    elif player == False and bust == False and dealer == True and tie == False:
        print('Dealer wins!\n')

    elif player == False and bust == False and dealer == False and tie == True:
        print('It\'s a tie! No one wins!\n')
    
    return 1

main()

