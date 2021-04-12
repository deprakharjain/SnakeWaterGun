'''
    PROJECT FOR P1
    PROECT NAME--SNAKE🐍 WATER🌊 GUN🔫
    CREATED BY-->PIYUSH JAIN(191B185),,B6
                 PRAKHAR JAIN(191B188),,B6
                 RISHABH KUMAR SINGH(191B200),,B6
    Following are the rules of the game:
       a)Snake vs. Water: Snake drinks the water hence wins.
       b)Water vs. Gun: The gun will drown in water, hence a point for water.
       c)Gun vs. Snake: Gun will kill the snake and win.   '''         
import random

'''Function that checks the rules of the game'''

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True

'''Using random function computer chooses value between 1,2,3'''

print("Comp turn:Snake(s),Water(w),Gun(g)?")
randNo = random.randint(1,3)
if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="g"

'''User makes its selection'''

you=input("Your's turn:Snake(s),Water(w),Gun(g)?")
a= gameWin(comp,you)
print(f"computer choose {comp}")
print(f"you choose {you}")

'''Result is declared on the basis of system and user selection'''
if a==None:
    print("The game is a tie!")
elif a:
    print("You win!!")
else:
    print("you loose!!")