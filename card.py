import itertools
import random

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

suits = ['♦','♣','♥','♠']
facecards = ["J","Q","K","A"]



deck = list(itertools.product(vals, suits))
random.shuffle(deck)

#todo add function to "Reset" deck, or reinstantiate\
d_hand = []
p_hand = []

def deal():
    #for val, suit in deck[0:4]:
    #   print('%s%s' % (val, suit))
    drawcard(d_hand)
    drawcard(d_hand)
    drawcard(p_hand)
    drawcard(p_hand)

    # d_hand += deck.pop()
    # p_hand += deck.pop()

                                
def drawcard(player):
    player.append(deck.pop(0))


def status():
    
    print('Dealer has:',end=" ")
    eval(d_hand)

    for val, suit in d_hand:
        print('%s%s' % (val, suit),end=" ") #end=" ") necessary for printing properly
    print("\t\n")

    print("You have: ",end=" ")
    eval(p_hand)

    for val, suit in p_hand:
        print('%s%s' % (val, suit),end=" ")
    print("\t")
    
    ask = input("Do you (H)it or (S)tand?")

    if ask == 'h':
        drawcard(p_hand)
    elif ask == 's':
        pass


def eval(hand):
    total = 0

    for val in hand:  
        if(val[0]) in ("J","Q","K"):
            total += 10
        elif(val[0]) == 'A':
            total += 11
        else:
            total += int(val[0])
    
    print(total)


def prompt(x):
    if x == 'h':
        drawcard(p_hand)
    elif x == 'd':
        drawcard(d_hand)
   # else 
                                                                     


def run_game():
    deal()
    status()

run_game()


