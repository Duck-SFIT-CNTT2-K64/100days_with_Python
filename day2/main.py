# height = float(input())
# weight = input()

# BMI = int(weight) / (int(height) * int(height))
# print(BMI)

# age = input()
# result = (90 - int(age)) * 52
# print(f"You have {result} weeks left")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

result = round((bill + (bill * (tip/100))) / 7, 2)
print(f"Each person should pay: ${result}")