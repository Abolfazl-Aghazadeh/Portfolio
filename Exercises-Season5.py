# --------------------------1--------------------------
# from multiprocessing.util import MAXFD
#
# i = int(input("Enter a number: "))
# j = int(input("Enter another number: "))
#
# Max = max(i, j)
# Min = min(i, j)

# for i in range(Min, Max + 1):
#     print(i, end = " ")

# while i != j:
#     if i <= j:
#         print(i, end=" ")
#         i += 1
#     elif j <= i:
#         print(j, end=" ")
#         j += 1

# while Min <= Max:
#     print(Min, end=" ")
#     Min += 1

# --------------------------2--------------------------

# A = int(input("Enter a number: "))
# B = int(input("Enter another number: "))
# Min = min(A, B)
# for i in range(1, Min+1):
#     if A % i == 0 and B % i == 0:
#         print(i, end = " ")

# --------------------------3--------------------------

# A = int(input("Enter a number: "))
# B = int(input("Enter another number: "))
# Min = min(A, B)
# Divisor = []
# for i in range(1, Min + 1):
#     if A % i == 0 and B % i == 0:
#         Divisor.append(i)
# print(Divisor[-1])

# A = int(input("Enter a number: "))
# B = int(input("Enter another number: "))
# Min = min(A, B)
# for i in range(Min, 1, -1):
#     if A % i == 0 and B % i == 0:
#         print(i)
#         break

# --------------------------4--------------------------

# A = int(input("Enter a number: "))
# B = int(input("Enter another number: "))
# Max = max(A, B)
# Min = min(A, B)
# for i in range(1, Min + 1):
#     if (Max * i) % Min == 0:
#         print(Max * i)
#         break

# A = int(input("Enter a number: "))
# B = int(input("Enter another number: "))
# Max = max(A, B)
# Min = min(A, B)
# i = Max
# while i % Min != 0:
#     i += Max
# print(i)

# --------------------------5--------------------------

# Number = int(input("Enter a number: "))
# i = 0
# while Number > 0:
#     Number //= 10
#     i += 1
# print(i)

# --------------------------6--------------------------

# Num = int(input("Enter a number: "))
# i = 1
# while i <= Num:
#     print(" " * (Num - i), end="")
#     print("*" * i)
#     i += 1

# Num = int(input("Enter a number: "))
# for i in range(1, Num + 1):
#     print(" " * ( Num - i ), end="")
#     print("*" * i)

# --------------------------7--------------------------

# import random
# Names = ["Abolfazl", "Amirali", "Sajad", "Shohreh"]
# print(f"Choose a name in your mind and i will guss it. use this list: ", Names)
# Ask = input("Have you choose a name?(y/n) ")
# while Ask != "y":
#     print("Please choose a name in your mind and i will guss it.")
#     Ask = input("Have you choose a name?(y/n) ")
#     if Ask == "y":
#         print(f"Let me guss ... hhhuummm ... you choose: {Names[random.choice(range(len(Names)))]}")
#         Ask2 = input("Am i right?(y/n) ")
#         while Ask2 != "y":
#             print(f"Let me guss ... uummm ... you choose: {Names[random.choice(range(len(Names)))]}")
#             Ask2 = input("Am i right?(y/n) ")
#             if Ask2 == "y":
#                 print("HaHaHaHa")
#                 break

# --------------------------8--------------------------

# import random
# import string
#
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# symbols = string.punctuation
# numbers = string.digits
#
# All = lower + upper + symbols + numbers
#
# while True:
#     print("""Choose an option:
#     1) Create a password
#     2) Exit""")
#     Choice = input("Enter your choice: ")
#     if Choice == '1':
#         length = int(input("Enter length of password: "))
#         password = "".join(random.sample(All, length))
#         print(password)
#     elif Choice == '2':
#         break
#     else:
#         print("Invalid choice")

# --------------------------9--------------------------

# import time
# from os import system, name
# while True:
#     choice = input("Would you like to start? (y/n): ")
#     if "y" in choice.lower():
#         hour = int(input("How many hours do you have?: "))
#         minute = int(input("How many minutes do you have?: "))
#         second = int(input("How many seconds do you have?: "))
#         total = hour * 60 * 60 + minute * 60 + second
#         print("Timer will start in 3 seconds...")
#         time.sleep(3)
#         while total >= 1:
#             print(total)
#             total -= 1
#             time.sleep(1)
#             if name == "nt":
#                 system("cls")
#             elif name == "posix":
#                 system("clear")
#         print("Timer will stop in 3 seconds...")
#         time.sleep(3)
#     elif "n" in choice.lower():
#         print("Goodbye!")
#         break
#     else:
#         print("Sorry, I didn't understand that. Please try again.")

# --------------------------10--------------------------





























