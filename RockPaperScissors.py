print("  Let's Play the Game---->>")
print("""
______           _     ______                       _____      _                    
| ___ \         | |    | ___ \                     /  ___|    (_)                   
| |_/ /___   ___| | __ | |_/ /_ _ _ __   ___ _ __  \ `--.  ___ _ ___ ___  ___  _ __ 
|    // _ \ / __| |/ / |  __/ _` | '_ \ / _ \ '__|  `--. \/ __| / __/ __|/ _ \| '__|
| |\ \ (_) | (__|   <  | | | (_| | |_) |  __/ |    /\__/ / (__| \__ \__ \ (_) | |   
\_| \_\___/ \___|_|\_\ \_|  \__,_| .__/ \___|_|    \____/ \___|_|___/___/\___/|_|   
                                 | |                                                
                                 |_|                                                
""")
v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
list = [rock, paper, scissors]
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if (my_choice==0) or (my_choice==1) or (my_choice==2)==True:
    me = list[my_choice]
    print(me)
    com = random.randint(0, len(list) - 1)
    computer_choice = list[com]
    print("computer choose: ")
    print(computer_choice)
    if my_choice == 0:
        if com == 0:
            print("match draw!")
        elif com == 1:
            print("Sorry, You lose")
        elif com == 2:
            print("Congrats You win")
    if my_choice == 1:
        if com == 1:
            print("match draw!")
        elif com == 2:
            print("Sorry, You lose")
        elif com == 0:
            print("Congrats You win")
    if my_choice == 2:
        if com == 2:
            print("match draw!")
        elif com == 0:
            print("Sorry, You lose")
        elif com == 1:
            print("Congrats You win")
else:
    print("please enter right input")