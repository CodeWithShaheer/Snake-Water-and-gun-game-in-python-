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
    if((computer-you)==1 or (computer-you)==-2 ):
        print("You Win!")
    else:
        print("You lose!")