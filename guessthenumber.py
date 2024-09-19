import random

s=(input("range of number from 0 to :-"))
if s.isdigit() :
    s=int(s)
    if s<=0:
        print("next time type number above 0!")
        quit()
else:
    print("type numbers next time")
    quit()    
m=random.randint(0,s)
k=0

while True:
    s=input("make a guess :-")
    if s.isdigit() :
        s=int(s)
        if s<=0:
            print("next time type number above 0!")
            quit()
    else:
        print("type numbers next time")
        quit()  
    if s>m:
        print("you got it wrong!")
        print("you are guessing above the number")
        k+=1
    elif(s<m):
        print("you got it wrong!")
        print("you are guessing below the number")
        k+=1
    else:
        k+=1
        break

print("you got it !")
print("you got it in",k,"chance")