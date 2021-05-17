import random

playerHand = []
dealerHand = []

playerScore = 0
dealerScore = 0
playerNumCards = 0
dealerNumCards = 0

playerHasHardAce = False
dealerHasHardAce = False
roundOver = False

playerGameScore = 0
dealerGameScore = 0

def update():
    global playerScore
    global dealerScore
    global playerNumCards
    global dealerNumCards
    global playerHasHardAce
    global dealerHasHardAce

    playerScore = 0
    dealerScore = 0
    playerNumCards = 0
    dealerNumCards = 0
    playerHasHardAce = False
    dealerHasHardAce = False

    for i in range(len(playerHand)):
        playerNumCards += 1
        if playerHand[i] == 1 and playerScore <= 11:
            playerHasHardAce = True
            playerScore += 10
        playerScore += playerHand[i]

    if playerScore >= 22 and playerHasHardAce == True:
        playerScore -= 10
        playerHasHardAce = False

    for i in range(len(dealerHand)):
        dealerNumCards += 1
        if dealerHand[i] == 1 and dealerScore <= 11:
            dealerHasHardAce = True
            dealerScore += 10
        dealerScore += dealerHand[i]

    if dealerScore >= 22 and dealerHasHardAce == True:
        dealerScore -= 10
        dealerHasHardAce = False

def dealCards(hand):
    randomCard = random.randint(1, 10)
    hand.append(randomCard)
    update()

def showHands(turn):
    if turn == "playerTurn":
        print("\n|" + "-"*20 + " " +str(playerGameScore) + " : " + str(dealerGameScore) + " " + "-"*20 + "|")
        print("\nPlayer's Hand: ", playerScore, "\n-------------")
        for i in range(len(playerHand)):
            if playerHand[i] == 1:
                print("Ace")
            elif playerHand[i] == 10:
                print("Face Card")
            else:
                print(playerHand[i])
        print("\nDealer's Hand: ", dealerHand[0], "\n-------------")
        print(dealerHand[0])
        print("[HIDDEN]")
    if turn == "dealerTurn":
        print("\n|" + "-"*20 + " " +str(playerGameScore) + " : " + str(dealerGameScore) + " " + "-"*20 + "|")
        print("\nPlayer's Hand: ", playerScore, "\n------------------")
        for i in range(len(playerHand)):
            if playerHand[i] == 1:
                print("Ace")
            elif playerHand[i] == 10:
                print("Face Card")
            else:
                print(playerHand[i])
        print("\nDealer's Hand: ", dealerScore, "\n------------------")
        for i in range(len(dealerHand)):
            if dealerHand[i] == 1:
                print("Ace")
            elif dealerHand[i] == 10:
                print("Face Card")
            else:
                print(dealerHand[i])

dealCards(playerHand)
dealCards(playerHand)
dealCards(dealerHand)
dealCards(dealerHand)

showHands("playerTurn")

while True:
    answer = input("\nHit or Stand (h or s)? ")
    if answer.lower() == "h":
        dealCards(playerHand)
        showHands("playerTurn")
        if playerScore >= 22:
            print("\nPlayer has BUSTED! Dealer Wins!")
            playerGameScore -= 10
            dealerGameScore += 10
            roundOver = True
            break
        elif playerNumCards >= 5 and playerScore < 22:
            print("\nPlayer has 5 cards and is under 22! Player WINS!")
            playerGameScore += 10
            dealerGameScore -= 10
            roundOver = True
            break
        else:
            pass
    elif answer.lower() == "s":
        break
    else:
        print("\nIncorrect input try again!")

if roundOver == False:
    while True:
        if dealerScore <= 15:
            dealCards(dealerHand)
            showHands("dealerTurn")
            if dealerScore >= 22:
                print("\nDealer has BUSTED! Player WINS!")
                dealerGameScore -= 10
                playerGameScore += 10
                break
            elif dealerNumCards == 5 and dealerScore < 22:
                print("\nDealer hsa 5 cards and is under 22! Dealer WINS!")
                dealerGameScore += 10
                playerGameScore -= 10
                break
            else:
                showHands("dealerTurn")
                break

if roundOver == False:
    if playerScore > dealerScore:
        playerGameScore += 10
        dealerGameScore -= 10
    elif dealerScore > playerScore:
        dealerGameScore += 10
        playerGameScore -= 10
    elif playerScore == dealerScore:
        dealerGameScore += 10
        playerGameScore -= 10

    showHands("dealerTurn")