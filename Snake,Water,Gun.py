
#Author - Advait More. Social Media; Twitter - @Adva1tMore, Reddit - u/north_2006

import random #Random module is an built-in module used to generate psedu-random numbers. 

def GameWin(Computer, You): #Def declares a function "GameWin" 

# An example and use of Conditional expressions. 

    if Computer == You:
        return None
    elif Computer =="S": 
        if You == "W":
            return False 
        elif You == "G":
            return True
        
    elif Computer == "W":
        if You == "G":
            return False
        
        elif You == "S":
            return True
    
    elif Computer == "G" :
        if You == "S": 
            return False 
        elif You == "W":
            return True


# Here I will use random module that I imported in line 1. Random module In this case will chose from 1 to 3. 

print("Computer's Turn: Snake(S) Water(W) or Gun(G)") 
randomNumber = random.randint(1, 3) # Random Module will choose from 1 to 3. 
if randomNumber == 1: 
    Computer = "S"                  # 1 == "S"
elif randomNumber == 2:
    Computer = "W"                  # 2 == "W"
elif randomNumber == 3:             
    Computer = "G"                  # 3 == 'G 

You = input("Your Turn: Choose Snake(S) Water(R) or Gun(G): ")
a = GameWin(Computer, You)

print(F'Computer chose {Computer}')
print(f'You chose {You}')

if a == None:
    print("The game is tied!")
elif a:
    print("You Won!🥳")
else: 
    print("You Lose!😔")

