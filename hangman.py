import random
import string 

words=["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive"
       ,"abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","exuberant","exultant","eye","eyes","fabulous","face","fail","faint","fairies",
       "faithful","fall","fallacious","false","familiar","famous","fanatical","fancy","fang","fantastic","far","farm","fascinated","fast","fasten","fat","faulty","fax","fear","fearful"
       ,"fearless","feeble","feeling","feigned","female","five","fix","fixed","flag","flagrant","flaky","flame","flap","flash","flashy","flat","flavor","flawless","flesh","flight","flimsy",
       "flippant","float","flock","flood","floor","flow","flower","fluttering","foolish","foot","force","foregoing","forgetful","fork","form","fortunate","found","four","fowl","fragile","frail",
       "free","freezing","frequent","fresh","fretful","friction","friend","friendly","friends","frighten","frightened","frightening","fuel","full","fumbling","functional","funny","furniture","furry","furtive",
       "future","futuristic","fuzzy","gabby","gainful","gamy","gaping","garrulous","gorgeous","government","governor","grab","graceful","grade","grain","grandfather","grandiose","grandmother","grape",
       "grass","grate","grateful","gratis","gray","grease","greasy","great","greedy","green","greet","grey","grieving","grin","grip","groan","groovy","grotesque","grouchy","ground","group","growth","grubby","gruesome"
       ,"grumpy","guarantee","guard","guarded","guess","guide","guiltless","guitar","gullible","gun","gusty","guttural","habitual","hair","haircut","half","hall","hallowed","halting","hammer","hand","handle","hands",
       "handsome","handsomely","handy","hang","hanging","hapless","happen","happy","harass","harbor","hard","hard-to-find","harm","harmonious","harmony","harsh","hat","hate","hateful","haunt","head","heady","heal",
       "health","healthy","heap","heartbreaking","heat","heavenly","heavy","hellish","help","helpful","helpless","hesitant","hideous","high"]

def hangman():
    word=random.choice(words)
    word_list=list(word)
    word_loop=list(word)
    alphabet=list(string.ascii_lowercase)
    user_letters=[]
    count=0
    max_attempts = len(word)+5
    attempts = 0
    print("TOTAL NUMBER OF ATTEMPTS: ",max_attempts)
    while word_loop and attempts<max_attempts:
        print("LETTERS USED: ",user_letters)
        user=input("ENTER YOUR GUESS CHARACTER: ").lower()
        if user in alphabet:
            count=count+1
            attempts+=1
            print("YOU HAVE",max_attempts-attempts,"ATTEMPTS LEFT")
            user_letters.append(user)
            alphabet.remove(user)
            word_loop = [char for char in word_loop if char != user]
              
            for char in word_list:
                if char in user_letters:
                    print(char,end=" ")  
                else:
                    print("_",end=" ")
            print("")
                    

                    
        elif user in user_letters:
            print("ALREADY USED CHARACTER")
            count=count+1
            attempts+=1
            print("YOU HAVE",max_attempts-attempts,"ATTEMPTS LEFT")
        else:
            print("INVALID CHARACTER")
            
    if len(word_loop)==0:
        print()
        print("CONGULATION, YOU GUESSED IT RIGHT, ITS THE WORD",word)
        print(f"IT TOOK YOU {count} TURNS TO GUESS THE WORD")
        print(f"YOU HAD {max_attempts-attempts} TURNS LEFTED FROM {max_attempts}")
    else:
        print("SORRY , YOUR ATTEMPTS OVER!!! YOU COULDN'T GUESS THE WORD")
        print("THE WORD WAS:",word)
    

print("WELCOME TO HANGMAN GAME")
print("Welcome to Hangman! Can you guess the hidden word? \nThe computer has selected a random word, and it's up to you to guess it letter by letter before the hangman is drawn.\nGood luck!")
s=input("PRESS s to start the game: ")
if s=="s":
    hangman()
else:
    print("INVALID")
    
