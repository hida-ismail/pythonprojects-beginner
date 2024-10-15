'''import random
def game(x):
    points_user=0
    points_comp=0
    for i in range(x):
        user=input("CHOOSE r for ROCK, p for PAPER OR s for SCISSORS: ").lower()
        l=["r","p","s"]
        comp=random.choice(l)
        print("COMPUTER CHOICE: ",comp)
        if (user=="r" and comp=="p") or (user=="p" and comp=="s") or (user=="s" and comp=="r"):
            print("YOU LOSE!!!,POINT ADDED TO COMPUTER")
            points_comp+=1
        elif user==comp:
            print("ITS A TIE, NO POINT ADDED")
        elif (user=="p" and comp=="r") or (user=="s" and comp=="p") or (user=="r" and comp=="s"):
            print("YOU WIN!!!, POINT ADDED TO USER")
            points_user+=1
        else:
            print("INVALID ROUND")
    winner(x,points_user,points_comp)

def winner(x,points_user,points_comp):
    print()
    print("TOTAL ROUNDS: ",x)
    print("NO. OF TIE ROUND: ",x-(points_user+points_comp))
    if points_user>points_comp:
        print("CONGULATION, YOU WIN THE GAME!!")
        print("YOUR POINTS:",points_user)
        print("COMPUTERS POINTS: ",points_comp)  
    elif points_user==points_comp:
        print("ITS A TIE")
        print("YOUR POINTS:",points_user)
        print("COMPUTERS POINTS: ",points_comp)  
    else:
        print("SORRY,YOU LOST THE GAME, TRY AGAIN")
        print("YOUR POINTS:",points_user)
        print("COMPUTERS POINTS: ",points_comp)      
            
x=int(input("Enter how many times you want to play the game: "))
game(x)
    
'''

import random

    
def game(x):
    points_user=0
    points_comp=0
    for i in range(x):
        user=input("CHOOSE r for ROCK, p for PAPER OR s for SCISSORS: ").lower()
        while user not in ["r","p","s"]:
            print("INVALID CHOICE")
            user=input("CHOOSE AGAIN r for ROCK, p for PAPER OR s for SCISSORS: ").lower() 
        l=["r","p","s"]
        comp=random.choice(l)
        print("COMPUTER CHOICE: ",comp)
        result=winner(user,comp)
        if result=="computer":
            print("YOU LOSE!!!,POINT ADDED TO COMPUTER")
            points_comp+=1
        elif result=="Tie":
            print("ITS A TIE, NO POINT ADDED")
        else:
            print("YOU WIN!!!, POINT ADDED TO USER")
            points_user+=1
    winner_by_points(x,points_user,points_comp)
        

def winner(user,comp):
    if (user=="r" and comp=="p") or (user=="p" and comp=="s") or (user=="s" and comp=="r"):
        return "computer"
    elif user==comp:
        return "Tie"
    else:
        return "user"
        
    

def winner_by_points(x,points_user,points_comp):
    print()
    print("TOTAL ROUNDS: ",x)
    print("NO. OF TIE ROUND: ",x-(points_user+points_comp))
    if points_user>points_comp:
        print("CONGULATION, YOU WIN THE GAME!!")
        print("YOUR POINTS:",points_user)
        print("COMPUTERS POINTS: ",points_comp)  
    elif points_user==points_comp:
        print("ITS A TIE")
        print("YOUR POINTS:",points_user)
        print("COMPUTERS POINTS: ",points_comp)  
    else:
        print("SORRY,YOU LOST THE GAME, TRY AGAIN")
        print("YOUR POINTS:",points_user)
        print("COMPUTERS POINTS: ",points_comp)      
            
x=int(input("Enter how many times you want to play the game: "))
game(x)
