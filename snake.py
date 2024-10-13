import random as ran

def reset():
    print("Do you want to play again ? (y/n)")
    inn = str(input()) 
        
    if inn == 'y':
        home()
    elif inn == 'n':
        print("Play again")  
    

def logic(computer, name):
    scoreU:int = 0
    scoreC:int = 0
    for i in range(1,6):
        print("Enter 's' for snake, 'w' for water, 'g' for gun ")
        user = str(input())
        print("computer choose ",computer)
        
        if computer == 'w':
            if user == 's':
                scoreU += 1
            else:
                scoreC += 1
        elif computer == 's':
            if user == 'g':
                scoreU += 1
            else:
                scoreC += 1
        elif computer == 'g':
            if user == 'w':
                scoreU += 1
            else:
                scoreC += 1
        elif (computer == 'w' and user == 'w') or (computer == 's' and user == 's') or (computer == 'g' and user == 'g'):
            continue
        
    if scoreC > scoreU :
        print("Computer is the winner\n\n")   
        reset()  
      
    elif scoreC < scoreU:
        print(f"{name} is the the winner")        
        reset()  

            

def home():

    print("You have 5 chance to win this game")
    print("Enter your name = ")
    name = str(input())

    num = ran.randrange(1,4)
    if num == 1:
        computer = 's'
    elif num == 2:
        computer = 'w'
    elif num == 3:
        computer = 'g'
        
    logic(computer, name)


home()