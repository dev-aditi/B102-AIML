
#----------------------------------------------------------------------------------------------------------------
# 1. Even or Odd Function
#----------------------------------------------------------------------------------------------------------------
# Q1. Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

# def is_even(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(is_even(4))
# print(is_even(7))


#----------------------------------------------------------------------------------------------------------------
# 2. Largest of Two Numbers
#----------------------------------------------------------------------------------------------------------------
# Q2. Write a function largest(a, b) that returns the larger number.

# def largest(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(largest(10, 20))


#----------------------------------------------------------------------------------------------------------------
# 3. Print Numbers
#----------------------------------------------------------------------------------------------------------------
# Q3. Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)
# print_numbers(5)


#----------------------------------------------------------------------------------------------------------------
# 4. Sum of Numbers
#----------------------------------------------------------------------------------------------------------------
# Q4. Write a function sum_n(n) that returns the sum of numbers from 1 to n.

# def sum_n(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# print(sum_n(5))


#----------------------------------------------------------------------------------------------------------------
# 5. Multiplication Table
#----------------------------------------------------------------------------------------------------------------
# Q5. Write a function table(n) that prints the multiplication table of n from 1 to 10.

# def table(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)
# table(5)


#----------------------------------------------------------------------------------------------------------------
# 6. Count Even Numbers
#----------------------------------------------------------------------------------------------------------------
# Q6. Write a function that takes a list and returns how many even numbers it contains.

# def count_even(lst):
#     count = 0
#     for i in lst:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_even([1, 2, 3, 4, 6]))


#----------------------------------------------------------------------------------------------------------------
# 7. Find Maximum
#----------------------------------------------------------------------------------------------------------------
# Q7. Without using max(), write a function that returns the largest number in a list.

# def find_max(lst):
#     largest = lst[0]
#     for i in lst:
#         if i > largest:
#             largest = i
#     return largest
# print(find_max([10, 25, 5, 40, 15]))


#----------------------------------------------------------------------------------------------------------------
# 8. FizzBuzz
#----------------------------------------------------------------------------------------------------------------
# Q8. Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# fizzbuzz()


#----------------------------------------------------------------------------------------------------------------
# 9. Palindrome Checker
#----------------------------------------------------------------------------------------------------------------
# Q9. Write a function that returns True if a string is a palindrome.

# def palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False
# print(palindrome("madam"))
# print(palindrome("hello"))


#----------------------------------------------------------------------------------------------------------------
# 10. Count Vowels
#----------------------------------------------------------------------------------------------------------------
# Q10. Write a function that counts the vowels in a string.

# def count_vowels(s):
#     count = 0
#     for i in s.lower():
#         if i in "aeiou":
#             count += 1
#     return count
# print(count_vowels("Hello World"))


#----------------------------------------------------------------------------------------------------------------
# 11. Second Largest Number
#----------------------------------------------------------------------------------------------------------------
# Q11. Write a function that returns the second largest number in a list without using sort().
# def second_largest(lst):
#     largest = float('-inf')
#     second = float('-inf')
#     for i in lst:
#         if i > largest:
#             second = largest
#             largest = i
#         elif i > second and i != largest:
#             second = i
#     if second == float('-inf'):
#         return "No second largest number"
#     return second
# print(second_largest([10, 20, 30, 40, 50]))


#----------------------------------------------------------------------------------------------------------------
# 12. Guessing Game
#----------------------------------------------------------------------------------------------------------------
# Q12. Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

# import random
# def guessing_game():
#     num = random.randint(1, 10)
#     while True:
#         guess = int(input("Guess a number between 1 and 10: "))
#         if guess == num:
#             print("Correct! You won!")
#             break
#         elif guess < num:
#             print("Too low! Try again.")
#         else:
#             print("Too high! Try again.")
# guessing_game()


#----------------------------------------------------------------------------------------------------------------
# 13. Grade Calculator
#----------------------------------------------------------------------------------------------------------------
# Q13. Write a function grade(marks) that:
# Returns "A" for marks >= 90
# Returns "B" for marks >= 80
# Returns "C" for marks >= 70
# Returns "D" for marks >= 60
# Otherwise returns "F".

# def grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"
# print(grade(95))
# print(grade(85))
# print(grade(75))
# print(grade(65))
# print(grade(40))
