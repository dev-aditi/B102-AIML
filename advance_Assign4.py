
#----------------------------------------------------------------------------------------------------------------
# 1. Even or Odd
#----------------------------------------------------------------------------------------------------------------
# Q1. Write a Python program to check whether a number is even or odd.

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


#----------------------------------------------------------------------------------------------------------------
# 2. Largest of Three Numbers
#----------------------------------------------------------------------------------------------------------------
# Q2. Write a program to find the largest of three numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest number:", a)
# elif b >= a and b >= c:
#     print("Largest number:", b)
# else:
#     print("Largest number:", c)


#----------------------------------------------------------------------------------------------------------------
# 3. Prime Number
#----------------------------------------------------------------------------------------------------------------
# Q3. Write a program to check whether a given number is prime.

# n = int(input("Enter a number: "))
# count = 0

# if n > 1:
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1

#     if count == 2:
#         print("Prime number")
#     else:
#         print("Not a prime number")
# else:
#     print("Not a prime number")


#----------------------------------------------------------------------------------------------------------------
# 4. Fibonacci Series
#----------------------------------------------------------------------------------------------------------------
# Q4. Write a program to print the Fibonacci series up to n terms.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


#----------------------------------------------------------------------------------------------------------------
# 5. Factorial Using Loop
#----------------------------------------------------------------------------------------------------------------
# Q5. Write a program to find the factorial of a number using a loop.

# n = int(input("Enter a number: "))
# fact = 1

# if n < 0:
#     print("Factorial is not defined for negative numbers")
# else:
#     for i in range(1, n + 1):
#         fact = fact * i

#     print("Factorial:", fact)


#----------------------------------------------------------------------------------------------------------------
# 6. Reverse a String Without Using [::-1]
#----------------------------------------------------------------------------------------------------------------
# Q6. Write a program to reverse a string without using [::-1].

# s = input("Enter a string: ")
# rev = ""

# for i in s:
#     rev = i + rev

# print("Reversed string:", rev)


#----------------------------------------------------------------------------------------------------------------
# 7. Palindrome Checker
#----------------------------------------------------------------------------------------------------------------
# Q7. Write a program to check whether a string is a palindrome.

# s = input("Enter a string: ")
# rev = ""

# for i in s:
#     rev = i + rev

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")


#----------------------------------------------------------------------------------------------------------------
# 8. Count Vowels and Consonants
#----------------------------------------------------------------------------------------------------------------
# Q8. Write a program to count the number of vowels and consonants in a string.

# s = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for i in s.lower():
#     if i.isalpha():
#         if i in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)


#----------------------------------------------------------------------------------------------------------------
# 9. Sum of All Elements in a List
#----------------------------------------------------------------------------------------------------------------
# Q9. Write a program to find the sum of all elements in a list.

# lst = [10, 20, 30, 40, 50]
# total = 0

# for i in lst:
#     total += i

# print("Sum of elements:", total)


#----------------------------------------------------------------------------------------------------------------
# 10. Largest and Smallest Element Without max() or min()
#----------------------------------------------------------------------------------------------------------------
# Q10. Write a program to find the largest and smallest element in a list.

# lst = [10, 25, 5, 40, 15]

# largest = lst[0]
# smallest = lst[0]

# for i in lst:
#     if i > largest:
#         largest = i

#     if i < smallest:
#         smallest = i

# print("Largest element:", largest)
# print("Smallest element:", smallest)


#----------------------------------------------------------------------------------------------------------------
# 11. Remove Duplicate Elements from a List
#----------------------------------------------------------------------------------------------------------------
# Q11. Write a program to remove duplicate elements from a list.

# lst = [1, 2, 3, 2, 4, 1, 5, 3]
# result = []

# for i in lst:
#     if i not in result:
#         result.append(i)

# print("List without duplicates:", result)


#----------------------------------------------------------------------------------------------------------------
# 12. Count Frequency of Each Element Using Dictionary
#----------------------------------------------------------------------------------------------------------------
# Q12. Write a program to count how many times each element appears in a list.

# lst = [1, 2, 3, 2, 1, 4, 2]
# freq = {}

# for i in lst:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print("Frequency:", freq)


#----------------------------------------------------------------------------------------------------------------
# 13. Second Largest Number in a List
#----------------------------------------------------------------------------------------------------------------
# Q13. Write a program to find the second-largest number in a list.

# lst = [10, 20, 30, 40, 50]

# largest = float('-inf')
# second = float('-inf')

# for i in lst:
#     if i > largest:
#         second = largest
#         largest = i

#     elif i > second and i != largest:
#         second = i

# if second == float('-inf'):
#     print("No second largest number")
# else:
#     print("Second largest number:", second)


#----------------------------------------------------------------------------------------------------------------
# 14. Sort a List Without sort() or sorted()
#----------------------------------------------------------------------------------------------------------------
# Q14. Write a program to sort a list without using sort() or sorted().

# lst = [5, 2, 8, 1, 9, 3]

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]

# print("Sorted list:", lst)


#----------------------------------------------------------------------------------------------------------------
# 15. Return Only Even Numbers Using Function
#----------------------------------------------------------------------------------------------------------------
# Q15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.

# def even_numbers(lst):
#     result = []

#     for i in lst:
#         if i % 2 == 0:
#             result.append(i)

#     return result

# print(even_numbers([1, 2, 3, 4, 5, 6, 8]))


#----------------------------------------------------------------------------------------------------------------
# 16. Frequency of Each Character in a String
#----------------------------------------------------------------------------------------------------------------
# Q16. Write a program to find the frequency of each character in a string.

# s = input("Enter a string: ")
# freq = {}

# for i in s:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print("Character frequency:", freq)


#----------------------------------------------------------------------------------------------------------------
# 17. Check Whether Two Strings Are Anagrams
#----------------------------------------------------------------------------------------------------------------
# Q17. Write a program to check whether two strings are anagrams of each other.

# s1 = input("Enter first string: ").lower()
# s2 = input("Enter second string: ").lower()

# if len(s1) == len(s2):
#     if sorted(s1) == sorted(s2):
#         print("Anagram")
#     else:
#         print("Not anagram")
# else:
#     print("Not anagram")


#----------------------------------------------------------------------------------------------------------------
# 18. Find All Duplicate Values in a List
#----------------------------------------------------------------------------------------------------------------
# Q18. Write a program to find all duplicate values in a list.

# lst = [1, 2, 3, 2, 4, 1, 5, 3]
# duplicates = []

# for i in lst:
#     if lst.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)

# print("Duplicate values:", duplicates)


#----------------------------------------------------------------------------------------------------------------
# 19. Find the Longest Word in a Sentence
#----------------------------------------------------------------------------------------------------------------
# Q19. Write a program that takes a sentence and finds the longest word.

# sentence = input("Enter a sentence: ")
# words = sentence.split()

# longest = ""

# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print("Longest word:", longest)
# print("Length:", len(longest))


#----------------------------------------------------------------------------------------------------------------
# 20. Student Marks and Grade Program
#----------------------------------------------------------------------------------------------------------------
# Q20. Create a simple student marks program that:
# Accepts marks for 5 subjects.
# Calculates the total and percentage.
# Assigns a grade.
# Displays whether the student passed or failed.

# marks = []

# for i in range(1, 6):
#     m = float(input("Enter marks for subject " + str(i) + ": "))
#     marks.append(m)

# total = 0

# for i in marks:
#     total += i

# percentage = total / 5

# print("Total marks:", total)
# print("Percentage:", percentage, "%")

# if any(m < 35 for m in marks):
#     print("Result: Fail")
#     print("Grade: F")

# elif percentage >= 90:
#     print("Grade: A")
#     print("Result: Pass")

# elif percentage >= 80:
#     print("Grade: B")
#     print("Result: Pass")

# elif percentage >= 70:
#     print("Grade: C")
#     print("Result: Pass")

# elif percentage >= 60:
#     print("Grade: D")
#     print("Result: Pass")

# else:
#     print("Grade: F")
#     print("Result: Fail")

