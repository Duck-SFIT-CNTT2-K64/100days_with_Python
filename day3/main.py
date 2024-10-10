# height = float(input())
# weight = int(input())

# result = weight / (height ** 2)

# if result < 18.5:
#   print(f"Your BMI is {result}, you are underweight.")
# elif result >= 18.5 and result < 25:
#   print(f"Your BMI is {result}, you have a normal weight.")
# elif result >= 25 and result < 30:
#   print(f"Your BMI is {result}, you are slightly overweight.")
# elif result >= 30 and result < 35:
#   print(f"Your BMI is {result}, you are obese.")
# else:
#   print(f"Your BMI is {result}, you are clinically obese.")




# year = int(input())

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not leap year")





# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()
# add_pepperoni = input()
# add_extra = input()

# bill = 0

# if size == 'S':
#     bill += 15
#     if add_pepperoni == 'Y':
#         bill += 2
#     if add_extra == 'Y':
#         bill += 1

# elif size == 'M':
#     bill += 20
#     if add_pepperoni == 'Y':
#         bill += 3
#     if add_extra == 'Y':
#         bill += 1

# elif size == 'L':
#     bill += 25
#     if add_pepperoni == 'Y':
#         bill += 3
#     if add_extra == 'Y':
#         bill += 1

# print(f"Your final bill is: ${bill}.")




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
road = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''')
if road == 'left':
    lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if lake == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if door == 'red':
            print("\nBurned by fire.\nGame Over.")
        elif door == 'blue':
            print("\nEaten by beasts.\nGame Over.")
        elif door == 'yellow':
            print("\nYou win!")
        else:
            print("\nGame Over.")
    else:
        print("\nAttacked by trout.\nGame Over.")
else:
    print("\nFall into a hole.\nGame Over.")