import random
import my_module

# random_interger = random.randint(1, 10)
# # print(random_interger)

# # print(my_module.pi)
# random_float = random.random() #Tạo ra 1 số float ngẫu nhiên từ 0 -> 1
# print(random_float)

# random_float = random.random() * 5 # muốn chuyển between từ 0 -> 1 thì *5 lên




# game = random.randint(0, 1)
# if game == 1:
#     print("Heads")
# else:
#     print("Tails")




#Lists
# Tinh_o_Vietnam = ["Ha Noi", "Ho Chi Minh", 'Hung Yen', 'Ha Nam', 'Da Nang']
# Huyen_o_HungYen = ['Kim Dong', 'Khoai Chau', 'Duc Hop', 'Dong Long']
# fullOf = [Tinh_o_Vietnam, Huyen_o_HungYen]
# print(fullOf[0][3])
# print(Tinh_o_Vietnam[random.randint(0, 4)]) #Nếu dùng số âm thì sẽ in từ dưới lên, bắt đầu từ -1
# Tinh_o_Vietnam.append("Tay Ninh") #Thêm phần tử vào cuối danh sách
# print(Tinh_o_Vietnam)
# Tinh_o_Vietnam.extend(['Thai Nguyen', 'Nghe An']) # Thêm 1 chuỗi vào cuối danh sách
# print(Tinh_o_Vietnam)





#Đánh dấu X trong ô đã được chọn
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# position = input()
# letter = position[0].lower()
# abc = ['a', 'b', 'c']
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = 'X'

# print(f"{line1}\n{line2}\n{line3}")





#Game kéo, búa, bao
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
game = input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n")

index = ['rock', 'paper', 'scissors']
# game_index = index.index(game)
if game == '0':
    print(rock)
    print("Computer choose:")
    game_computer = random.randint(0, 2)
    if game_computer == 0:
        print(rock)
        print("\nYou Draw!\n")
    elif game_computer == 1:
        print(paper)
        print("\nComputer win!\n")
    else:
        print(scissors)
        print("\nYou win!")
elif game == '1':
    print(paper)
    print("Computer choose:")
    game_computer = random.randint(0, 2)
    if game_computer == 0:
        print(rock)
        print("\nYou win!\n")
    elif game_computer == 1:
        print(paper)
        print("\nYou draw!\n")
    else:
        print(scissors)
        print("\nComputer win!")
else:
    print(scissors)
    print("Computer choose:")
    game_computer = random.randint(0, 2)
    if game_computer == 0:
        print(rock)
        print("\nComputer win!\n")
    elif game_computer == 1:
        print(paper)
        print("\nYou win!\n")
    else:
        print(scissors)
        print("\nYou draw!")