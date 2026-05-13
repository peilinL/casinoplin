import random
#check for aces
def playeracecheck():
    #global the variables ts caused me so much headache bc i forgot that u had to global variables
    global playeraces, playeramount
    if playeramount > 21 and playeraces > 0:
        playeramount = playeramount - 10
        playeraces = playeraces - 1

#trigger the dealer drawing
def dealerdraw():
    #global the variables
    global dealeramount, dealeraces, balance, bet, game
    while dealeramount < 17:
        card = random.randint(0,12)
        dealeramount = dealeramount + cardnumber[card]
        dealercards.append(card)
        if card == 0:
            dealeraces = dealeraces + 1
        if dealeramount > 21 and dealeraces > 0:
            dealeramount = dealeramount - 10
            dealeraces = dealeraces - 1
    print("Dealer's cards are:",end=" ")
    for card in dealercards:
        print(cardnumberdisplayed[card], end=" ")
    print("["+str(dealeramount)+"]")
    if dealeramount > playeramount  and dealeramount <= 21:
        print("You lost.")
        print("New balance:",balance)
    elif dealeramount > 21:
        print("Dealer busts. You win.")
        balance = balance + 2*bet
        print("New balance:",balance)
    elif dealeramount < playeramount:
        print("You win.")
        balance = balance + 2*bet
        print("New balance:",balance)
    elif dealeramount == playeramount:
        print("A tie. Push.")
        balance = balance + bet
    game = False

#i have to make two functions for split command and theyre literally just ace check...

def reset():
    global dealeraces, playeraces
    global dealeramount, playeramount
    global dealercards, playercards
    global firstturncheck
    dealeraces = 0
    playeraces = 0
    dealeramount = 0
    playeramount = 0
    dealercards = []
    playercards = []
    firstturncheck = True

#setup the cards and stuff
cardnumber = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cardnumberdisplayed = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#card is in game loop
game = False

dealeramount = 0
playeramount = 0
#imma add bet amount later ts is so hard

#finally i can make balance and bet
balance = 1000
bet = 0
#WIP #comment 2: probably still WIP might be done
#make minimum bet 1
#dealer aces and player aces
dealeraces = 0
playeraces = 0

#here is the turn conditionals to make sure you don't split or double on turns that are not the first
firstturncheck = True



while True:
    command = input(" ")
    parts = command.split()
    if len(parts) == 0:
        continue
    elif parts[0] == ".help":
        print("Commands: ")
        print(".bal: check balance")
        print(".bj [bet amount]: start blackjack with bet amount.")
        print(".hit: receive one card.")
        print(".stand: stop receiving cards.")
        print(".double: double bet and receive only one more card.")
        print(".split: split cards into two hands if cards are same.")
    #imma add double and split later ight?
    elif parts[0] == ".bal":
        print("Your balance is:",balance)
    elif parts[0] == ".bj" and len(parts) != 2:
        print("Please enter bet.")
        continue
    elif parts[0] == ".bj" and len(parts) == 2 and not parts[1].isdigit():
        print("Please enter integer bet.")
        continue
    elif parts[0] == ".bj" and len(parts) == 2 and parts[1].isdigit():
        bet = int(parts[1])
        if bet > balance:
            print("Insufficient balance, bet set to maximum value")
            bet = balance
            game = True
        if bet < 1:
            print("Bet must be at least 1.")
            continue
        print("Game started, bet is",bet)
        reset()
        game = True
        balance = balance - bet

        for i in range(2):
            card = random.randint(0,12)
            playeramount = playeramount + cardnumber[card]
            playercards.append(card)
            if card == 0:
                playeraces = playeraces + 1
            if playeramount > 21 and playeraces > 0:
                playeramount = playeramount - 10
                playeraces = playeraces - 1
                #####HERE IS THE CONDITIONAL FOR ACE ADD THIS TO A DIFFERENT PART OF CODE AS WELL
        print("Your cards:", end=" ")
        
        for card in playercards:
            print(cardnumberdisplayed[card], end=" ")
        print("[",playeramount,"]")

        
        upcard = random.randint(0,12)
        dealeramount = dealeramount + cardnumber[upcard]
        dealercards.append(upcard)
        print("Dealer's card up is:", cardnumberdisplayed[dealercards[0]])
#continuing to lobby commands
    elif parts[0] == ".hit" and not game:
        print("Game not started yet.")
    elif parts[0] == ".stand" and not game:
        print("Game not started yet.")
    elif parts[0] == ".double" and not game:
        print("Game not started yet.")
    elif parts[0] == ".split" and not game:
        print("Game not started yet.")
    elif parts[0] not in [".help", ".bj", ".hit", ".stand",".double",".split"]:
        continue
#continue game    
    while game and playeramount <= 21:        
        command = input(" ")
        parts = command.split()
#hit command
        if parts[0] == ".hit":
            card = random.randint(0,12)
            playeramount = playeramount + cardnumber[card]
            playercards.append(card)
            #conditional statement for aces
            if card == 0:
                playeraces = playeraces + 1
            playeracecheck()
            print("Your cards:", end=" ")
            for card in playercards:
                print(cardnumberdisplayed[card], end=" ")
            print("["+str(playeramount)+"]")
            if playeramount > 21:
                print("Bust! You lose.")
                print("New balance:",balance)
                game = False
                reset()
                break
            else:
                firstturncheck = False
#standing command

        elif parts[0] == ".stand":
            print("Your total is:",playeramount)
            dealerdraw()
            reset()
            break
#doubling command check for first turn

        elif parts[0] == ".double" and firstturncheck == False:
            print("Cannot double on turns that are not the first.")
            continue
#doubling command

        elif parts[0] == ".double":
            firstturncheck = False
            if bet * 2 > balance:
                print("Insufficient balance to double.")
                continue
            balance = balance - bet
            bet = 2*bet
            card = random.randint(0,12)
            playeramount = playeramount + cardnumber[card]
            playercards.append(card)
            if card == 0:
                playeraces = playeraces + 1
            playeracecheck()
            print("Your cards:", end=" ")
            for card in playercards:
                print(cardnumberdisplayed[card], end=" ")
            print("["+str(playeramount)+"]")
            if playeramount > 21:
                print("Bust! You lose.")
                print("New balance:",balance)
                game = False
                reset()
                break
            dealerdraw()
            reset()
            break

#splitting command check for first term
        elif parts[0] == ".split" and firstturncheck == False:
            print("Cannot split on turns that are not the first.")
            continue

#splitting command check for balance
        elif parts[0] == ".split" and bet > balance:
            print("Insufficient balance to split.")
            continue

#splitting command check for same card
        elif parts[0] == ".split" and playercards[0] != playercards[1]:
            print("Cards are not the same.")
            continue

#splitting command
        elif parts[0] == ".split":
            firstturncheck = False
            balance = balance - bet
            hand1 = []
            hand2 = []
            hand1.append(playercards[0])
            hand2.append(playercards[1])
            hand1aces = 0
            hand2aces = 0
            playinghand1 = True
            playinghand2 = False
            hand1lost = False
            hand2lost = False
            hand1amount = cardnumber[playercards[0]]
            hand2amount = cardnumber[playercards[1]]
        
            card = random.randint(0,12)
            hand1.append(card)
            hand1amount += cardnumber[card]

            if card == 0:
                hand1aces += 1

            if hand1amount > 21 and hand1aces > 0:
                hand1amount -= 10
                hand1aces -= 1


            card = random.randint(0,12)
            hand2.append(card)
            hand2amount += cardnumber[card]

            if card == 0:
                hand2aces += 1

            if hand2amount > 21 and hand2aces > 0:
                hand2amount -= 10
                hand2aces -= 1
            print("Hand one:",end=" ")
            for card in hand1:
                print(cardnumberdisplayed[card], end=" ")
            print("["+str(hand1amount)+"]")

            print("Hand two:",end=" ")
            for card in hand2:
                print(cardnumberdisplayed[card], end=" ")
            print("["+str(hand2amount)+"]")
            while playinghand1:
                command = input(" ")
    #hitting command
                if command == ".hit":
                    card = random.randint(0,12)
                    hand1amount = hand1amount + cardnumber[card]
                    hand1.append(card)
                    #conditional statement for aces
                    if card == 0:
                        hand1aces = hand1aces + 1
                    if hand1amount > 21 and hand1aces > 0:
                        hand1amount = hand1amount - 10
                        hand1aces = hand1aces - 1
                    print("Hand one:", end=" ")
                    for card in hand1:
                        print(cardnumberdisplayed[card], end=" ")
                    print("["+str(hand1amount)+"]")
                    if hand1amount > 21:
                        print("Bust! Hand one lost.")
                        hand1lost = True
                        playinghand2 = True
                        print("Now playing hand two.")
                        playinghand1 = False

    #standing command
                elif command == ".stand":
                    print("Hand one:",hand1amount)
                    playinghand2 = True
                    print("Now playing hand two.")
                    playinghand1 = False


            while playinghand2:
                command = input(" ")
    #hitting command
                if command == ".hit":
                    card = random.randint(0,12)
                    hand2amount = hand2amount + cardnumber[card]
                    hand2.append(card)
                    #conditional statement for aces
                    if card == 0:
                        hand2aces = hand2aces + 1
                    if hand2amount > 21 and hand2aces > 0:
                        hand2amount = hand2amount - 10
                        hand2aces = hand2aces - 1
                    print("Hand two:", end=" ")
                    for card in hand2:
                        print(cardnumberdisplayed[card], end=" ")
                    print("["+str(hand2amount)+"]")
                    if hand2amount > 21:
                        print("Bust! Hand two lost.")
                        hand2lost = True
                        playinghand2 = False

    #standing command
                elif command == ".stand":
                    print("Hand two:",hand2amount)
                    playinghand2 = False
            if not playinghand1 and not playinghand2:
                while dealeramount < 17:
                    card = random.randint(0,12)
                    dealeramount = dealeramount + cardnumber[card]
                    dealercards.append(card)
                    if card == 0:
                        dealeraces = dealeraces + 1
                    if dealeramount > 21 and dealeraces > 0:
                        dealeramount = dealeramount - 10
                        dealeraces = dealeraces - 1
                print("Dealer's cards are:",end=" ")
                for card in dealercards:
                    print(cardnumberdisplayed[card], end=" ")
                print("["+str(dealeramount)+"]")
                if not hand1lost: 
                    if dealeramount > hand1amount  and dealeramount <= 21:
                        print("You lost.")
                    elif dealeramount > 21:
                        print("Dealer busts. Hand one win.")
                        balance = balance + 2*bet
                    elif dealeramount < hand1amount:
                        print("You win.")
                        balance = balance + 2*bet
                    elif dealeramount == hand1amount:
                        print("Hand one tie. Push.")
                        balance = balance + bet
                    game = False

                if not hand2lost: 
                    if dealeramount > hand2amount  and dealeramount <= 21:
                        print("You lost.")
                        balance = balance
                        print("New balance:",balance)
                    elif dealeramount > 21:
                        print("Dealer busts. Hand two win.")
                        balance = balance + 2*bet
                        print("New balance:",balance)
                    elif dealeramount < hand2amount:
                        print("Hand two win.")
                        balance = balance + 2*bet
                        print("New balance:",balance)
                    elif dealeramount == hand2amount:
                        balance = balance + bet
                        print("Hand two tie. Push.")
                reset()

        #testing code        
        elif parts[0] == "devtest3238":

            playercards = [int(parts[1]), int(parts[2])]

            playeramount = 0
            playeraces = 0

            for card in playercards:
                playeramount += cardnumber[card]

                if card == 0:
                    playeraces += 1

            playeracecheck()

            print("Test hand:", end=" ")

            for card in playercards:
                print(cardnumberdisplayed[card], end=" ")

            print("[" + str(playeramount) + "]")

            
            

            

                
