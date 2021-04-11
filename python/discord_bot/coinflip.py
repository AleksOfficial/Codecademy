import random

'''
Basic Requirements

    User Story: As a user I want to be able to guess the outcome of a random coin flip(heads/tails).
    User Story: As a user I want to clearly see the result of the coin flip.
    User Story: As a user I want to clearly see whether or not I guessed correctly.

Additional Challenges

Intermediate Challenge

    User Story: As a user I want to clearly see the updated guess history (correct count/total count).
    User Story: As a user I want to be able to quit the game or go again after each cycle.

Advanced Challenge

Let’s see if we can expand upon this challenge - what if instead of 2 options, there were 6?

User Story: As a user I want to be able to guess the outcome of a 6-sided dice roll (1-6), with the same feature set as the coin flip (see above).

    You can add this directly to the existing program you’ve already written! As an additional challenge see if you can build the program such that the the user can choose between the two guessing games at startup, and possibly even switch after each cycle.
'''

def welcome_message():
    
    print('''\nHello There!
Choose your option:

    1. - Flip a Coin (without prediction)
    2. - Flip a Coin (with prediction)
    3. - Roll a dice (with prediction)
    4. - Roll a dice (without prediction)
    5. - Exit
    ''')

def rates(total_plays,total_wins):
    try:
        coin_flip_rate = total_wins[0]/total_plays[1]*100
        dice_rate = total_wins[1]/total_plays[2]*100
        print('''Rates:
    - Coin flip: {}
    - Coin flip /w prediction: {}/{} - {:.2f} %
    - Dice prediction : {}/{} - {:.2f} %
    - Dice plays: {}'''.format(total_plays[0],total_wins[0],total_plays[1],coin_flip_rate,total_wins[1],total_plays[2],dice_rate,total_plays[3]))
    except:
        return

def coin_flip(amount_of_outcomes, choice=None):
    flip = random.randint(1,amount_of_outcomes)
    if choice is not None:
        if amount_of_outcomes <3:
            if choice == flip:
                if flip == 1:
                    print("Congrats! You won! your Choice: Heads")
                if flip == 2: 
                    print("Congrats! You won! your Choice: Tails")
                return True,flip
            else:
                if choice == 1:
                    print("Oups. You lost! your Choice: Heads")
                if choice ==2:
                    print("Oups. You lost! your Choice: Tails")
                return False,flip
        else:
            if choice == flip:
               print("Congrats! You won! your Choice: {}".format(choice))
               return True,flip
            else:
               print("Oups. You lost! your Choice: {}".format(choice))
               return False,flip
            
            print("Result: {}".format(flip))
    else:
        if amount_of_outcomes <3:
            if flip == 1:
                print("Outcome: Heads")
            if flip == 2:
                print("Outcome: Tails")
        else:
            print("Outcome: {}".format(flip))
        return flip
        

def evaluate(choice,history,total_plays,total_wins):

    if choice == 1:
        Outcome = coin_flip(2)
        history[0].append(Outcome)
        total_plays[0] +=1

    elif choice == 2:
        prediction = 0
        while prediction not in range(1,3):
            prediction = input('''What will you predict?
                1 = heads
                2 = tails
                : ''')
            try:
                prediction = int(prediction)
                if(prediction not in range(1,3)):
                    raise ConversionError
            except:
                print("Invalid Input you cunt.")
        win_loss, Outcome = coin_flip(2,prediction)
        history[1].append(Outcome)
        total_plays[1]+=1
        if win_loss:
            total_wins[0]+=1

    elif choice == 3:
        prediction = 0
        while prediction not in range(1,7):
            prediction = input('''What will you predict? (1-6): 
            : ''')
            try:
                prediction = int(prediction)
                if prediction not in range(1,7):
                    raise ConversionError
            except:
                print("Invalid Input you cunt.")

        win_loss,Outcome = coin_flip(6,prediction)
        history[2].append(Outcome)
        total_plays[2]+=1
        if win_loss:
            total_wins[1]+=1
        
    elif choice == 4:
        Outcome = coin_flip(6)
        history[3].append(Outcome)
        total_plays[3]+=1

    

history = [[] for x in range(0,4)]
total_plays = [0 for x in range(0,4)]
total_wins = [0 for x in range(0,2)]
user_choice = 0
while user_choice !=5:    
    welcome_message()
    rates(total_plays,total_wins)    
    try:
        user_choice = int(input())
    
        if user_choice in range(1,6):
            evaluate(user_choice,history,total_plays,total_wins)
        else:
            raise ConversionError
    except:
        print("Invalid input u cunt.")
    
    