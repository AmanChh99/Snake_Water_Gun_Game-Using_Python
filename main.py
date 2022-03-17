import random

def game(comp,you):
    if(comp == you):
        return(None)
    elif(comp == 's'):
        if(you == 'g'):
            return(True)
        elif(you == 'w'):
            return(False)
    elif(comp == 'g'):
        if(you == 's'):
            return(False)
        elif(you == 'w'):
            return(True)
    elif(comp == 'w'):
        if(you == 'g'):
            return(False)
        elif(you == 's'):
            return(True)

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)

if(randNo == 1):
    comp = 's'
elif(randNo == 2):
    comp = 'w'
elif(randNo == 3):
    comp = 'g'


you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = game(comp,you)
print(f"Comp Chose: {comp}")
print(f"You Chose: {you}")
if(a == None):
    print("There is a Tie")
elif(a == False):
    print("You Lose")
else:
    print("You Win")
