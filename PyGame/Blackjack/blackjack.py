import random
from os import system
#functions
def clear():
    _ = system("cls")

def welcome_message():
    welcome_string='''Welcome to BlackJack!
Take a seat at our wonderful table! We garuantee that there is a fair chance to win at our game.
We offer a game for 7 players at a time. Also, there will be a set amount of card decks.
Therefore, cards will not be randomly generated.

You can also choose to play multiple boxes. Allowing for a faster game to be played.

Good Luck and Have Fun!          
'''
    return welcome_string

def help_string():
    rules= '''
The goal is to get as close as possible to 21 without going over 21!
Blackjack is a 21 (Ace and a 10-Card) straight at the beginning (paid 3:2)
Here are your possible Moves:
    - Stand: You take no more card
    - Hit: You take a card. you can then take another card if you wish.
    
    - Double: You double your bet. after that, you will take another card and your run has finished.
    - Split: If you happen to have 2 same cards, you can split these into two seperate Boxes. each of these boxes have the same bet.
        - if you split 2 Aces, you can take only one card on each box
    
    -Insurance: in case the dealer has a ten-card or an Ace, you can bet on an insurance
     which pays 2:1. If the dealer has a BlackJack, you win with your insurance.
\n'''
    return rules

def two_same_cards(total_cards):
    if len(total_cards) >1:
        compare1 = total_cards[-2][0]
        compare2 = total_cards[-1][0]
        if compare1 == compare2:
            return True
        else:
            return False
        

def calculate_score(total_cards):
    score = 0    
    for x in total_cards:
        if x[0]<10:
            score+=x[0]
            score+=1
        elif x[0] > 9:
            score+=10 
    return score 

def Name_of_cards(Card):
    name=""
    if Card[0] < 1:
        name +="Ace "
    elif Card[0] > 0 and Card[0] <10:
        name += str(Card[0]+1) + " "
    elif Card[0] == 10:
        name+= "Jack "
    elif Card[0] == 11:
        name+= "Queen "
    elif Card[0] == 12:
        name+= "King "
    if Card[1]==0:
        name+= "Hearts"
    elif Card[1]==1:
        name+= "Diamonds"
    elif Card[1]==2:
        name+= "Spades"
    else:
        name+= "Clubs"
    return name

def show_hand(Deck):
    hand_string =""
    for i in Deck:
        hand_string+=(Name_of_cards(i))
        hand_string+="\n"
    return hand_string

def all_false(choices):
    for j in range(1,5):
        choices[j] = False
    return choices

def not_enough_funds(choices):
    choices[2] = False
    choices[3] = False
    choices[4] = False

def has_ace(carddeck):
    for i in carddeck:
        if i[0] == 0:
            return True
    return False

def options(choices,Blackjack,Status,score1,score2,Dealer_hand,player_hand,player_name,help,lost_bet = 0):
    total_string = ""
    lost_string ="BUSTED!\n\nYou lost {} - went over 21\n".format(lost_bet)
    Blackjack_string="\n$$$ BLACKJACK! $$$\n you won {}".format(lost_bet)
    
    dealerscore_string = "Dealer's hand: {}\n".format(show_hand(Dealer_hand))
    player_hand_string = "Your Hand: \n{}".format(show_hand(player_hand))
    
    score_string = "Current score: {}".format(score1)
    second_score_string="\n"
    if score2 >0 and score2 < 22:
        second_score_string = " or {}\n".format(score2)
        
    score_string += second_score_string
    choice_string="Choose your Move: \n"
    if choices[0]:
        choice1_string="1 = Stand\n"
        choice_string+=choice1_string
    if choices[1]:
        choice2_string="2 = Hit\n"
        choice_string+=choice2_string
    if choices[2]:
        choice3_string="3 = Double\n"
        choice_string+=choice3_string
    if choices[3]:
        choice4_string="4 = Split\n"
        choice_string+=choice4_string
    if choices[4]:
        choice5_string="5 = Ace Split\n"
        choice_string+=choice5_string
    choice6_string = "6 = Help"
    choice_string += choice6_string
    if Blackjack:
        total_string += Blackjack_string
    if not Status:
        total_string += lost_string
    if help:
        total_string += help_string()
    total_string += dealerscore_string
    total_string += "\n{} - Bet: {}\n".format(player_name,lost_bet)
    total_string += player_hand_string
    total_string += score_string
    
    total_string +=choice_string
    return total_string
    
        
def splits_false(choices):
    choices[3] = False
    choices[4] = False
  
#Classes
class player:
    def __init__(self,name,id):
        self.id=id
        self.name = name
        self.credit = 1000
        self.credit_difference = 0
        
    def credit_change(self,amount):
        self.credit +=amount
        self.credit_difference +=amount
    
    def betting(self,amount):
        amount = amount*-1
        self.credit_change(amount)
        
    def win(self,amount):
        self.credit_change(amount)
    
    def fundcheck(self,amount):
        if self.credit >= amount:
            return True
        else: 
            return False
    def show_funds(self):
        print("Balance: {}".format(self.credit))
        return self.credit
        
class cards:
    def __init__(self, amount_of_decks):
        self.amount_of_decks = amount_of_decks
        self.decks = []
        self.discarded_cards = []
        self.set_up_decks()
    
    def set_up_decks(self):
        for carddeck in range(self.amount_of_decks):
            deck = []
            for y in range(4):
                for x in range(13):
                    deck.append([x,y])
            self.decks+=deck
    
    def draw_card(self):
        if self.decks != []:
            card = random.choice(self.decks)
            self.decks.remove(card)
        else:
            print("Deck is out of Cards! Reshuffling ...")
            self.decks = self.decks + self.discarded_cards
            self.discarded_cards = []
            return self.draw_card()
        return card
    
    def discard_cards(self,total_deck):
        self.discarded_cards = self.discarded_cards + total_deck

class Boxes:
    def __init__(self,player_id=None):
        self.subboxes = [[]]
        self.bets = []
        self.id = player_id
        self.status = []
        self.insurance = 0
        self.final_score = []
        self.Black_jack = False
    
    def add_card(self,carddeck,subbox):
        new_card=carddeck.draw_card()
        self.subboxes[subbox].append(new_card)
    
    def add_insurance(self,amount,player):
        self.insurance = amount
        player.betting(amount)
        
    def add_bet(self,position,bet):
        self.bets[position]+=bet
    
    def new_subbox(self,previous_bet,position):
        self.subboxes.append([])
        self.status.append(None)
        self.bets.append(previous_bet)
        double_card=self.subboxes[position].pop(-1)
        self.subboxes[-1].append(double_card)
        self.status.append(2)
        
    def Blackjack_check(self,position):
        if self.subboxes[position][0][0] == 0 and self.subboxes[position][1][0] >8: 
            return True
        elif self.subboxes[position][1][0] == 0 and self.subboxes[position][0][0] >8:
            return True
        else:
            return False
        
class table:
    def __init__(self,dealer_credit):
        self.topboxes =[0 for x in range(7)]
        self.remaining_box_count=7
        self.dealer = []
        self.total_cards = []
        self.dealer_credit = dealer_credit
        self.dealer_final_score = 0
        self.dealer_status = True
        self.dealer_blackjack = False
        
    def player_settingup_boxes(self,player_id,position):
        new_box = Boxes(player_id)
        self.topboxes[position]=new_box
    
    def player_lost(self,position,bets):
        lost_money = bets[position]
        bets[position]-=lost_money
        self.dealer_credit += lost_money
   
clear()      
print(welcome_message())
players = []

amount_of_players = int(input("How many players are there?\n: "))

amount_of_decks = int(input("with how many decks do you wish to play?\n: "))

for i in range(1,amount_of_players+1):
    
    name = input("what is the name of player {}? :".format(i))
    if name == "":
        name = "Player {}".format(i)
    players.append(player(name,i))

#Setting up the game
cards_in_game = cards(amount_of_decks)
dealer_credit = 0



while True:
    new_table = table(dealer_credit)
    #Distributing Boxes
    for x in range(len(players)):
        new_table.player_settingup_boxes(players[x].id,x)
        new_table.remaining_box_count -= 1
    if new_table.remaining_box_count >0:
        for x in range(len(players)):
            print(players[x].name)
            if input("Do you wish to play additional Boxes? 1 = True,0 = False :") == "1":
                additional_boxes= int(input("How many additional Boxes do you want to play? :"))
                while new_table.remaining_box_count < additional_boxes:
                    print("Invalid input. Try again.")
                    additional_boxes = int(input(": "))
                for y in range(additional_boxes):
                    new_table.player_settingup_boxes(players[x].id,7-new_table.remaining_box_count)
                    new_table.remaining_box_count -=1
    #Placing Bets
    #while(True):
    clear()
    count = 1
    for x in new_table.topboxes:
        index = 0
        if x != 0:
            index = x.id-1
            print(players[index].name)
            players[index].show_funds()
            player_bet = int(input("Place your bet for Box {}!\n: ".format(count)))
            while True:
                if player_bet%5 != 0:
                    print("Invalid bet. Bet can be only a multiple of 5. Please try again.")
                    player_bet= int(input(": "))
                elif not players[index].fundcheck(player_bet):
                    print("Insufficient funds. Please try again.")
                    player_bet= int(input(": "))
                else:
                    break
            print("Bet placed! {}\n".format(player_bet))
            x.bets.append(player_bet)
            x.status.append(2)
            players[index].betting(player_bet)

        count+=1
    #Distributing Cards
   
    dealer_card = cards_in_game.draw_card()
    new_table.dealer.append(dealer_card)
    for i in range(2):
        for x in new_table.topboxes:
            if x !=0:
                x.add_card(cards_in_game,0)
    
    help = False
    #Now the game begins
    for x in new_table.topboxes:
        if x !=0:
            #rewrite as a while
            y = 0
            amount_splitted_decks = len(x.subboxes)
            while y < amount_splitted_decks:
                clear()
                #1.stand 
                #2.hit_bool 
                #3.double_bool
                #4.Split
                #5.ace_split
                choices = [True for x in range(6)]               
                while(True):
                    if len(x.subboxes[y])>1 and y == 0:
                        if x.Blackjack_check(y):
                                x.Black_jack = True
                                all_false(choices)
                    if len(x.subboxes[y])>1:
                        if two_same_cards(x.subboxes[y]):
                            if x.subboxes[y][-1] == 0:
                                choices[3] = False
                            else:
                                choices[4] = False                
                        else:
                            splits_false(choices)
                    else:
                            splits_false(choices)
                    
                    if not players[x.id-1].fundcheck(x.bets[y]):
                        not_enough_funds(choices)
                    
                    if len(x.subboxes[y])<2 and x.subboxes[y][0] == 0:
                        x.add_card(cards_in_game,y)
                        all_false(choices)
                    
                    score1 = calculate_score(x.subboxes[y])
                    score2 = 0
                    if has_ace(x.subboxes[y]):
                        score2=score1+10
                    bet = x.bets[y]
                    if score1 > 21:
                        x.status[y] = False
                        all_false(choices)
                        new_table.player_lost(y,x.bets)                    
                    clear()
                    print(options(choices,x.Black_jack,x.status[y],score1,score2,new_table.dealer,x.subboxes[y],players[x.id-1].name,help,bet))
                    help = False
                    player_choice = int(input(": "))
                    if player_choice == 1 and choices[0]:
                        if score1 > score2 or score2>21:
                            x.final_score.append(score1)
                        else:
                            x.final_score.append(score2)
                        break
                    elif player_choice == 2 and choices[1]:
                        x.add_card(cards_in_game,y)
                    elif player_choice == 3 and choices[2]:
                        x.bets[y] = x.bets[y]*2
                        x.add_card(cards_in_game,y)
                        for j in range(1,5):
                            choices[j] = False
                    elif player_choice == 4 and choices[3]:
                        amount_splitted_decks +=1
                        x.new_subbox(x.bets[y],y)
                    elif player_choice == 5 and choices[4]:
                        x.new_subbox(x.bets[y],y)
                    elif player_choice == 6:
                        help = True
                y+=1

    #Insurance 
    if new_table.dealer[0][0] == 0:
        for x in new_table.topboxes:
            if x!=0:
                for y in range(len(x.subboxes)):
                    if x.status[y] !=False:
                            print(players[x.id-1].name)
                            print("You can place an Insurance if you want to!")
                            insurance_bet = int(input(": "))
                            x.add_insurance(insurance_bet,players[x.id-1])
                        
    #giving the dealer his cards
    while True:
        dealer_card = cards_in_game.draw_card()
        new_table.dealer.append(dealer_card)
        if new_table.dealer[0][0] == 0 and new_table.dealer[1][0] >8:
            dealer_blackjack = True
            break
        dealer_score1 = calculate_score(new_table.dealer)
        dealer_score2 = 0
        #new_table.dealer_final_score = 0
        if has_ace(new_table.dealer):
            dealer_score2=dealer_score1 +10             
        if dealer_score2 > 16 and dealer_score2 <22 and dealer_score2 > dealer_score1 :
            new_table.dealer_final_score = dealer_score2
            break
        elif dealer_score1 > 16:
            new_table.dealer_final_score = dealer_score1
            if new_table.dealer_final_score >21:
                new_table.dealer_status = False
            break
        
    #Evaluation_Cardvalues
    clear()
    print("Dealer's hand: {}".format(show_hand(new_table.dealer)).replace("\n"," -> "))
    print("Dealer's score: {}".format(new_table.dealer_final_score))
    print("Blackjack: {}".format(new_table.dealer_blackjack))
    print("\n")
    for x in new_table.topboxes:
        higher_hand = 2
        if x!=0:
            index = x.id-1
            y = 0
            amount_splitted_decks = len(x.subboxes)
            while y<amount_splitted_decks:
                if x.Black_jack:
                    x.status[y] = False
                if new_table.dealer_blackjack:
                    x.status[y] = False         
                else:
                    if x.status[y] != False:
                        if new_table.dealer_status:
                            if new_table.dealer_final_score > x.final_score[y]:
                                #Dealer Higher Hand
                                x.status[y] = False
                                higher_hand = True
                            elif new_table.dealer_final_score == x.final_score[y]:
                                x.status[y] = 2
                            else:
                                x.status[y] = True
                        else:
                            x.status[y] = True
                #INSURANCE NEEDS TO BE PROGRAMMED
                if x.status[y] == True:
                    #players[index].win(x.bets[y]*2)
                    if new_table.dealer_status:
                        print(players[index].name +" won! - higher hand! Score: {}".format(x.final_score[y]))
                        players[index].win(x.bets[y]*2)
                    else: 
                        print(players[index].name +" won! - Dealer busted! Score: {}".format(x.final_score[y]))
                        players[index].win(x.bets[y]*2)
                elif x.Black_jack == True:
                    players[index].win(x.bets[y]*3/2+x.bets[y])
                    print(players[index].name +" won! - BLACKJACK!")
                elif  new_table.dealer_blackjack == True and x.insurance>0:
                    print(players[index].name +" won! - Insurance! Bet: {}".format(x.insurance))
                    players[index].win(x.insurance*2+x.insurance)
                elif new_table.dealer_blackjack == True:
                    print(players[index].name +" lost! - Dealer has BlackJack! Score: {}".format(x.final_score[y]))
                elif x.status[y] == 2:
                    print(players[index].name +" pushed! - Same Hand! Score: {}".format(x.final_score[y]))
                    players[index].win(x.bets[y])
                
                elif higher_hand:
                    print(players[index].name +" lost! - Dealer has higher hand! Score: {}".format(x.final_score[y]))
                elif x.status[y] == False:
                    print(players[index].name +" lost! - Busted! Score: {}".format(x.final_score[y]))

                
                print("Your Hand: {}".format(show_hand(x.subboxes[y])).replace("\n"," -> "))
                y+=1

    #Discarding Cards
    dealer_credit = new_table.dealer_credit
    for x in new_table.topboxes:
        if x!=0:
            for y in range(len(x.subboxes)):
                new_table.total_cards += x.subboxes[y]
    cards_in_game.discard_cards(new_table.total_cards)
    #checking if continue is true  
    if input("Continue? (y = yes)") !="y":
        break                
    
