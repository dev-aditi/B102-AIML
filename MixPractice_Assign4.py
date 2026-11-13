#----------------------------------------------------------------------------------------------------------------
#1. Data Types
#----------------------------------------------------------------------------------------------------------------
# Q1.Find the data type of every value in a mixed list.
# L1=["Aditi",20,"student",True,8.57]
# for value in L1:
#     print(value,(type(value)))
# print(type(L1))
# print(type("Aditi"))
# print(type(20))
# print(type("student"))
# print(type(True))
# print(type(8.57))

#-----------------------------------------------------------
# Q2. Convert a nested list into a tuple of tuples.

#--------------------------------------------------------------------------------------

# Q3.Remove all duplicate values from a mixed list while preserving the original order.

#----------------------------------------------------------------------------------------------------------------
# 2. Operators
#----------------------------------------------------------------------------------------------------------------
#Q1. Check whether a number is a power of 2 using operators
# num=int(input("enter any number : "))
# if num>0 and num & (num-1)==0:
#     print("number is power of 2")
# else:
#     print("num is not power of 2")

#-----------------------------------------------------------------

# Q2. Swap two numbers using bitwise XOR.
# n1=int(input("enter num1 : "))
# n2=int(input("enter num2 : "))
# print("before swapping num1 = ",n1, "num2 = ",n2)
# n1= n1 ^ n2
# n2= n1^n2
# n1=n1^n2
# print("after swapping num1 = ",n1,"num2 = ",n2)

#---------------------------------------------------------------------------------

# Q3.Find whether a number is divisible by both 4 and 6 using logical operators.
# num=int(input("enter any number : "))
# if num%4==0 and num%6==0 :
#     print("num is divisible by both 4 & 6:")
# else:
#     print("num is not divisible by both 4 & 6:")

#------------------------------------------------------------------------------------

# Q4.Calculate the total electricity bill using different unit rates.
# units = int(input("Enter electricity units: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + (units - 100) * 7
# elif units <= 300:
#     bill = (100 * 5) + (100 * 7) + (units - 200) * 10
# else:
#     bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 12
# print("Total electricity bill:", bill)

#-------------------------------------------------------------------------------------
# 3. Conditional Statements
#------------------------------------------------------------------------------------------
# Q1. Check whether three sides can form a triangle
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))
# if a + b > c and a + c > b and b + c > a:
#     print("Valid triangle")
# else:
#     print("Not a valid triangle")

#--------------------------------------------------------------------------------------------

# Q2. Determine the type of triangle(Equilateral, Isosceles, Scalene)
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Equilateral triangle")
#     elif a == b or b == c or a == c:
#         print("Isosceles triangle")
#     else:
#         print("Scalene triangle")
# else:
#     print("Invalid triangle")

#-------------------------------------------------------------------------------------

# Q3.Create a simple ATM menu (Withdraw, Deposit, Balance)
# balance = 5000
# print("1. Withdraw")
# print("2. Deposit")
# print("3. Balance")

# choice = int(input("Enter your choice: "))
# if choice == 1:
#     amount = int(input("Enter withdrawal amount: "))
#     if amount > 0 and amount <= balance:
#         balance -= amount
#         print("Withdrawal successful")
#     else:
#         print("Invalid amount or insufficient balance")
# elif choice == 2:
#     amount = int(input("Enter deposit amount: "))
#     if amount > 0:
#         balance += amount
#         print("Deposit successful")
#     else:
#         print("Invalid amount")
# elif choice == 3:
#     print("Your balance is:", balance)
# else:
#     print("Invalid choice")

#-------------------------------------------------------

# Q4. Calculate income tax based on different tax slabs.
# income = int(input("Enter your annual income: "))
# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = (income - 250000) * 0.05
# elif income <= 1000000:
#     tax = (250000 * 0.05) + (income - 500000) * 0.20
# else:
#     tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
# print("Income tax:", tax)

#----------------------------------------------------------------------------

# Q5. Create a menu-driven calculator using if-elif
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# choice = int(input("Enter your choice: "))
# if choice == 1:
#     print("Addition:", a + b)
# elif choice == 2:
#     print("Subtraction:", a - b)
# elif choice == 3:
#     print("Multiplication:", a * b)
# elif choice == 4:
#     if b != 0:
#         print("Division:", a / b)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid choice")



#-----------------------------------------------------------------------------
# 4. Loops
#------------------------------------------------------------------------------
# Q1. Print all prime numbers between 1 and n.
# n = int(input("Enter a number: "))
# for num in range(2, n + 1):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num)

#-----------------------------------------------------------------

# Q2.Find the factorial of a number using a loop.
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print("Factorial:", fact)

#------------------------------------------------------------

# Q3.Print the Fibonacci series up to n terms
# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

#---------------------------------------------------------

# Q4. Check whether a number is an Armstrong number.
# n = int(input("Enter a number: "))
# temp = n
# total = 0
# power = len(str(n))
# while temp > 0:
#     digit = temp % 10
#     total += digit ** power
#     temp //= 10
# if total == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

#---------------------------------------------------------

# Q5. Reverse a number and check if it is a palindrome.
# n = int(input("Enter a number: "))
# temp = n
# rev = 0
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# print("Reverse:", rev)
# if n == rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

#-------------------------------------------------------

# Q6. Find the Greatest Common Divisor (GCD) of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# while b != 0:
#     a, b = b, a % b
# print("GCD:", abs(a))



#--------------------------------------------------------------------------------------
# 5. Functions
#-----------------------------------------------------------------------------------------
# Q1. Write a function to check if a string is a palindrome.
# def palindrome(s):
#     if s == s[::-1]:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
# s = input("Enter a string: ")
# palindrome(s)

#--------------------------------------------------------------------------------------
# Q2. Write a function to count vowels and consonants in a string.
# def count_letters(s):
#     vowels = 0
#     consonants = 0
#     for ch in s.lower():
#         if ch.isalpha():
#             if ch in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1
#     print("Vowels:", vowels)
#     print("Consonants:", consonants)
# s = input("Enter a string: ")
# count_letters(s)

#--------------------------------------------------------------------------------------

# Q3.Create a function to calculate simple and compound interest.
# def interest(p, r, t):
#     si = (p * r * t) / 100
#     ci = p * (1 + r / 100) ** t - p
#     print("Simple Interest:", si)
#     print("Compound Interest:", ci)
# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))
# interest(p, r, t)

#--------------------------------------------------------------------------------------
# Q4. Write a function to return all factors of a number.
# def factors(n):
#     result = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             result.append(i)
#     return result
# n = int(input("Enter number: "))
# print("Factors:", factors(n))
#--------------------------------------------------------------------------------------

# Q5. Write a function to find the second-largest number in a list.
# def second_largest(lst):
#     unique = list(set(lst))
#     unique.sort()
#     if len(unique) >= 2:
#         return unique[-2]
#     else:
#         return "No second largest number"
# lst = [10, 20, 30, 40, 50]
# print("Second largest:", second_largest(lst))



#--------------------------------------------------------------------------------------
# 6. Lists
#--------------------------------------------------------------------------------------
# 1. Merge two lists without duplicates
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# result = []
# for i in a + b:
#     if i not in result:
#         result.append(i)
# print(result)


#--------------------------------------------------------------------------------------
# 2. Find the second-largest and second-smallest elements.
# lst = [10, 20, 30, 40, 50]
# unique = sorted(set(lst))
# if len(unique) >= 2:
#     print("Second smallest:", unique[1])
#     print("Second largest:", unique[-2])
# else:
#     print("Not enough unique elements")


#--------------------------------------------------------------------------------------
# 3. Rotate a list to the left by k positions
# lst = [1, 2, 3, 4, 5]
# k = int(input("Enter rotation value: "))
# k = k % len(lst)
# result = lst[k:] + lst[:k]
# print(result)


#--------------------------------------------------------------------------------------
# 4. Separate even and odd numbers into two lists.
# lst = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []
# for i in lst:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even:", even)
# print("Odd:", odd)


#--------------------------------------------------------------------------------------
# 5. Find the common elements between two lists.
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# common = []
# for i in a:
#     if i in b and i not in common:
#         common.append(i)
# print("Common elements:", common)




#--------------------------------------------------------------------------------------
#  7. Tuples & Sets
#--------------------------------------------------------------------------------------
# 1. Count the frequency of each element in a tuple.
# t = (1, 2, 3, 2, 1, 4, 2)
# for i in set(t):
#     print(i, ":", t.count(i))


#--------------------------------------------------------------------------------------
# 2. Find the union, intersection, and difference of two sets.
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print("Union:", a | b)
# print("Intersection:", a & b)
# print("Difference:", a - b)


#--------------------------------------------------------------------------------------
# 3. Check whether one set is a subset of another.
# a = {1, 2}
# b = {1, 2, 3, 4, 5}
# if a.issubset(b):
#     print("A is a subset of B")
# else:
#     print("A is not a subset of B")


#--------------------------------------------------------------------------------------
#  8. Dictionaries
#--------------------------------------------------------------------------------------
# 1. Count the frequency of words in a sentence.
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# print(freq)

#--------------------------------------------------------------------------------------
# 2. Create dictionary from two lists(keys and values).
# keys = ["name", "age", "city"]
# values = ["Aditi", 20, "Nashik"]
# result = dict(zip(keys, values))
# print(result)

#--------------------------------------------------------------------------------------
#  3. Sort a dictionary by its values.
# d = {"A": 50, "B": 20, "C": 80, "D": 40}
# result = dict(sorted(d.items(), key=lambda x: x[1]))
# print(result)

#--------------------------------------------------------------------------------------
# 9. File Handling
#--------------------------------------------------------------------------------------
#  1. Read a text file and count the number of lines, words, and characters.
# with open("sample.txt", "r") as file:
#     data = file.read()
# lines = data.splitlines()
# words = data.split()
# characters = len(data)
# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", characters)

#--------------------------------------------------------------------------------------

# ### 2. Copy only the even-numbered lines from one file to another.
# with open("sample.txt", "r") as file:
#     lines = file.readlines()
# with open("even.txt", "w") as file:
#     for i in range(len(lines)):
#         if (i + 1) % 2 == 0:
#             file.write(lines[i])
# print("Even lines copied successfully")


#--------------------------------------------------------------------------------------
# 10. Exception Handling
#--------------------------------------------------------------------------------------
# Q1. Handle invalid integer input using try-except.
# try:
#     n = int(input("Enter a number: "))
#     print("Number:", n)
# except ValueError:
#     print("Please enter a valid integer")

#--------------------------------------------------------------------------------------

# Q2. Handle file-not-found errors while reading a file
# try:
#     with open("sample.txt", "r") as file:
#         data = file.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found")



#--------------------------------------------------------------------------------------
#  11. Modules
#--------------------------------------------------------------------------------------
# Q1. Create a random password generator using the random and string modules.
# import random
# import string
# characters = string.ascii_letters + string.digits + string.punctuation
# length = int(input("Enter password length: "))
# if length > 0:
#     password = ""
#     for i in range(length):
#         password += random.choice(characters)
#     print("Password:", password)
# else:
#     print("Invalid password length")

#--------------------------------------------------------------------------------------

# Q2. Use the datetime module to calculate the number of days between two dates
# from datetime import datetime
# date1 = input("Enter first date (DD-MM-YYYY): ")
# date2 = input("Enter second date (DD-MM-YYYY): ")
# d1 = datetime.strptime(date1, "%d-%m-%Y")
# d2 = datetime.strptime(date2, "%d-%m-%Y")
# difference = abs((d2 - d1).days)
# print("Difference in days:", difference)
