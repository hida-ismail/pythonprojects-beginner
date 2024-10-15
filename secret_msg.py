# Write a python program to translate a message into secret code language. 
#Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning



import random
import string
def encoder(s):
    l1=s.split(" ")
    l2=[]
    for word in l1:
        if len(word)>=3:
            random_word=["acs","abh","hlq","hid","qlh","pwf"]
            r1=random.choice(random_word)
            r2=random.choice(random_word)
            st=r1+word[1:]+word[0]+r2
            l2.append(st)
        else:
            st=word[::-1]
            l2.append(st)
    a=" ".join(l2)
    print("ENCODED MSG: ",a)

def decoder(s):
    l1=s.split(" ")
    l2=[]
    for word in l1:
        if len(word)>=3:
            st=word[3:-3]
            st=st[-1]+st[:-1]
            l2.append(st)
        else:
            st=word[::-1]
            l2.append(st)
    decoded_msg=" ".join(l2)
    print("DECODED MSG: ",decoded_msg)
    
    


print("menu: ")
print("1. ENCODE A MSG")
print("2. DECODE A MSG")
choice=int(input("ENTER YOUR CHOICE:"))
s=input("ENTER MESSAGE: ")
if choice==1:
    encoder(s) 
elif choice==2:
    decoder(s)
else:
    print("invalid")
    
    

  