"""
1 for snake
-1 for water
0 for gun 
    
"""
# @ shaheer
import random
computer = random.choice([-1,0,1]) 
youstr = input("Enter your choice : ")
youdict = {"s":1,"w":-1,"g":0}
you = youdict[youstr]
reversedict  = {1: "Snake", -1: "Water", 0: "Gun"}
print(f"You choose {reversedict[you]}\nComputer choose {reversedict[computer]}")

if (computer==you):
    print("Draw!")
else:
    if(computer ==-1 and you == 1): #-2
        print("You win!")

    elif(computer ==-1 and you == 0): #-1
        print("You Lose!")

    elif(computer == 1 and you == -1): #2
        print("You lose!")

    elif(computer ==1 and you == 0): #1
        print("You Win!")

    elif(computer ==0 and you == -1): #1
        print("You Win!")

    elif(computer == 0 and you == 1): #-1
        print("You Lose!")

    else:
        print("Something went wrong!")
        
