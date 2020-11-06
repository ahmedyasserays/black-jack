# create the start of the game and setting players
import card
dealer = card.player("Dealer")
player = card.player("Player One")
player_money = 1000

play = True
while play:  # main game loop and card generating
    deck = card.deck()
    deck.shuffle()
    yet = True

    while yet:
        print("you have {} pounds".format(player_money))
        try:
            bet = int(input("enter bet: "))
            if 0 < bet <= player_money:
                player_money -= bet
                yet = False
            else:
                print("enter a valid value")
        except ValueError:
            print('enter a valid value')




    game = True  # small games loop and the full logic
    while game:

        # player getting cards
        player.player_withdraw(deck)
        player.player_withdraw(deck)
        print("you get: " + " and ".join(player.show()))
        print('total points: ', player.points())

        # dealer getting cards
        dealer.player_withdraw(deck)
        dealer.player_withdraw(deck)
        print("dealer have: ", dealer.show())

        # win and lose logic
        stay = True
        while stay:
            answer = input("do you want to hint or stay?\n")
            if answer.lower() == "hint" or answer.lower() == "h":
                print("you get: " + " and ".join(player.show()) + " with total points of " + str(player.points()))
                print(f"dealer get {dealer.show()} total points of " + str(dealer.points()))

                if player.points() > 21:  # busted
                    print(f"busted, you lose")

                elif player.points() > dealer.points():  # win
                    print(f"you win, you have total points of {player.points()} and dealer have {dealer.points()}")
                    player_money += 2*bet
                elif player.points() == dealer.points():  # draw
                    player_money += bet
                    print("it's draw you and the dealer have the same points")
                else:  # lose
                    print(f"you lose, you have total points of {player.points()} and dealer have {dealer.points()}")
                player.new_game()
                dealer.new_game()
                game = False
                stay = False

            elif answer.lower() == "stay" or answer.lower() == "s":
                if dealer.points() < 11:
                    dealer.player_withdraw(deck)
                player.player_withdraw(deck)
                print("you get: " + " and ".join(player.show()) + " with total points of " + str(player.points()))

    if player_money == 0:
        print("you have lost all your money, come back later")
        break
    answer = input("do you want to play again? 1 means yes 2 means no\n")
    if answer == "1":
        play = True
    else:
        play = False
