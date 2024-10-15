import random

def guess(x):
    num=random.randint(1,x)
    guess_number=0
    count=0
    while guess_number!=num:
        guess_number=int(input("Enter The Number: "))
        if guess_number<num:
            print(f"Sorry, guess again {guess_number} is too low")
            count+=1
        elif guess_number>num:
            print(f"Sorry, guess again {guess_number} is too High")
            count+=1
    print(f"congulations!!! You have guessed it right {num} is the random number")
    print(f"It took you {count} tries guesses to correctly guess the number....")
    
      


def guess_comp(x):
    """computer guess the input number"""
    guess=random.randint(1,x)
    count=0
    num=int(input("ENTER A NUMBER: "))
    print(f"{guess}")
    while guess!=num:
        if guess<num:
            print("GUESSED NUMBER IS TOO LOW")
            guess=random.randint(guess,x)
            count+=1
        elif guess>num:
            print("GUESSED NUMBER IS TOO HIGH")
            guess=random.randint(1,guess)
            count+=1
    print(f"computer guessed it right, number is {guess}")
    print(f"It took Computer {count} tries to correctly guess the number....")



def guess_computer(x):
    low=1
    high=x
    guess=random.randint(low,high)
    count=0
    feedback=" "
    while feedback!='correct':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"IS {guess} THE GUESSED NUMBER HIGH , LOW OR CORRECT : ").lower()
        if feedback=="high":
            high=guess-1
            count+=1
        elif feedback=="low":
            low=guess+1
            count+=1
        elif feedback=="correct":
            print(f"yay, COMPUTER GUESSED IT RIGHT, THE GUESS NUMBER IS {guess}")
        else:
            print("invalid")
            count="Nan"
            break
    
    print(f"It took Computer {count} tries to correctly guess the number....")


print("menu:")   
print("1. GUESS THE NUMBER BY USER ")      
print("2. GUESS THE NUMBER BY COMPUTER (AUTOMATICALLY), INPUTED BY THE USER  ")  
print("3. GUESS THE NUMBER BY COMPUTER ")   
ch=int(input("ENTER YOUR CHOICE (1-3): "))
if ch==1:
    x=int(input("ENTER THE RANGE: "))
    guess(x)
elif ch==2:
    x=int(input("ENTER THE RANGE: "))
    guess_comp(x)
elif ch==3:
    x=int(input("ENTER THE RANGE: "))
    guess_computer(x)    
else:
    print("Invalid")












