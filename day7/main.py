#step 1 in Hangman
# word_list = ["aardvark", "baboon", "camel"]
# import random
# choosen  = random.choice(word_list)
# print(f"the solution is {choosen}")
# for letter in choosen:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")




#step 2
# list = []
# for letter in choosen:
#     list += '_'




#step 3

# end_game = False
# while not end_game:
#     guess = input("Guess a letter: ").lower()
#     for position in range(len(choosen)):
#         letter = choosen[position]
#         if letter == guess:
#             list[position] = letter
#     print(list)    
#     if '_' not in list:
#         end_game = True
#         print('You Win!')





#step 4
from hangman_art import logo
from hangman_art import stages
from hangman_word import word_list
import random
print(logo)
choosen  = random.choice(word_list)
print(f"the solution is {choosen}")
list = []
for letter in choosen:
    list += '_'
number_stages = 6
end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(choosen)):
        letter = choosen[position]
        if letter == guess:
            list[position] = letter

    if guess not in list:
        number_stages -= 1
        if number_stages == 0:
            end_game = True
            print("You Lose!")

    print(stages[number_stages])
    print(f"{' '.join(list)}")

    if '_' not in list:
        end_game = True
        print("You Win!")
    elif number_stages == 0:
        end_game = True
        print("You Lose!")