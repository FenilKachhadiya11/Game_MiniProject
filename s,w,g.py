import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

    
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
        
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
        
print("comp turn : snak(s) , water(w) , gun(g)")

randNo = random.randint(1,3)

if randNo == 1 :
    comp = "s"
elif randNo == 2 :
    comp = "w"
elif randNo == 3 :
    comp = "g"
    
    
you = input("your turn : snak(s) , water(w) , gun(g)")

a = gamewin(comp,you)


print(f"comp choise : {comp}")
print(f"you choise : {you}")


if a == None:
    print("taie")
elif a:
    print("you win")
else:
    print("you loss")
