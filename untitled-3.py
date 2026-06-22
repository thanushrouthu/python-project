print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
direction = input("you are at a cross road. where do you wanna go ? left or right \n")
if direction == "left":
    choice = input("You have come to the lake. There is an island in the middle of the lake.Type wait to wait for a boat.Type swim to swim across\n")
    if choice == "wait" :
        color_door = input("You arrive at the island. There is house with 3 doors. one red one yellow and one blue.which color do you choose?\n ")
        if color_door == "yellow" :
            print("You found the treasure . You win!")
        elif color_door == "blue" :
            print("You enter a room of beasts. game over")
        elif color_door == "red" :
            print("You enter a room of beasts. game over")
        else :
            print("You choose a door that does not exist. game over")
    else :
     print("You get attacked by creatures. game over")
else :
    print("You fell into a hole. game over")