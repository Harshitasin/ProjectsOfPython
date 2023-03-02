print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a1=input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n' )
a1_new=a1.lower()
if a1=="left":
    a2=input('You come to a lake. Ther is an island in the middle of the lake? Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    a2_new=a2.lower()
    if a2_new=="wait":
        a3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        a3_new=a3.lower()
        if a3_new=="blue":
            print("Shit! You enter a room of beasts. Game over.")
        elif a3_new=="red":
            print("This is Fire room. Game over.")
        elif a3_new=="yellow":
            print("You choose the right door here is your treasure. You Win.")
        else:
            print("Door not exist with this letter.")
    elif a2_new=="swim":
        print("This lake is poissoness. Game Over.")
elif a1=="right":
    print("Wrong route Sorry! Game over.")
print("Do you like this Game?")


