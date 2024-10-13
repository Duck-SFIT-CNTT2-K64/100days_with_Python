# Examble 1:
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])  
total_height = 0
number_student = 0
average_height = 0
for i in student_heights:
  total_height += i
  number_student += 1
print(f"total height = {total_height}\nnumber of students = {number_student}")
print(f"average height = {round(total_height / number_student)}")





#Examble 2:
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest = 0
for i in student_scores:
  if i > highest:
    highest = i
print(f"The highest score in the class is: {highest}")



#Kiến thức:
for i in range(1, 11, 3): #range(start, stop, step) same as for(i = 1; i < 11; i += 3)
  print(i)





#Examble 3:
target = int(input())
sum = 0
for i in range(2, target + 1):
  if i % 2 == 0:
    sum += i
print(sum)






# Trò chơi fizzbuzz <-> Examble 4:
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)





#Project create a password generator
import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = []

for i in range(num_letters):
    password.append(random.choice(letters))

for i in range(num_symbols):
    password.append(random.choice(symbols))

for i in range(num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

password_list = ""

for i in password:
    password_list += i

print(f"Here is your password: {password_list}")