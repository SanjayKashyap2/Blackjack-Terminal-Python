dollars = input("How many dollars do you have?")
dollars = int(dollars)
import random

def drawcard():                                #drawing card function
    card = cardlist[random.randint(0, len(cardlist)-1)]
    cardlist.remove(cardlist[card])
    return card
    

infinite_Loop_Variable = 0
cardlist = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

while infinite_Loop_Variable == 0:
    if len(cardlist) <= 25:
        cardlist = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    print("...")
    gamble = input("you have "+str(dollars)+" dollars. How many dollars you want to gamble?")
    gamble = int(gamble)
    dollars = dollars - gamble

    card1 = drawcard()       #testing function here    
    card2 = drawcard()
    dealer = drawcard()
    points = card1 + card2
    
    outcome = 0
    while(outcome < 1):  #Loop begins here
        
        print("your cards add up to "+str(points)+" and the dealer's first card is a "+str(dealer)+".")
        command = input('If you would like to hit, type "hit". If you would like to stand, type "stand".')
        command = len(command) # 3 for hit & 4 for stand
        
        if int(command) < 4: #hitting
            card3 = drawcard
            points = points+card3
            print("You were given a "+str(card3)+".")
            if points > 21:
                outcome = 3   #user has busted
        else:  #standing
            print("You have chosen to stand")
            outcome = 2    #normal standing
    
    else:   #loop should end here, end game/results begin
    
        if outcome == 2: #didn't bust
            dealer2 = drawcard()              #Dealer logic
            dealer = dealer + dealer2
            print("The dealer showed their second card and it brings them up to "+str(dealer)+" points. You have "+str(points)+" points.")
        
            win_or_lose = int(dealer) - int(points)
            if int(win_or_lose) > 0:  #lost
                print('Sorry, but you lost to the dealer. Your remaining balance is '+str(dollars)+" dollars.")
            elif int(win_or_lose) < 0:   #User has more than dealer
                while (dealer - points) < 0: #dealer is hitting
                    card3 = drawcard()
                    dealer = dealer + card3
                    print("The dealer hit and now has "+str(dealer)+" points.")
                    if dealer > 21: #dealer busting
                        print("The dealer busted. You win!")
                        dollars = dollars + gamble*2
                    else:
                        if (dealer - points) == 0:
                            dollars = dollars + gamble
                            print("It's a draw. Your money has been refunded")
                        else:
                            print('The house has won.')
            else:
                dollars = dollars+gamble
                print("It's a draw! Your money was refunded")
        else: #should only be if outcome 3 (busting)
            print("It's a bust! You now have "+str(dollars)+" dollars. All that money is gone now. Do you feel better? You could've invested that you know.")
    if dollars <= 0:
        print("You ran out of money. Universe ending now.")
        infinite_Loop_Variable = 1
    else:
        infinite_Loop_Variable = 0

# git remote add origin https://github.com/SanjayKashyap2/Blackjack-Terminal-Python.git