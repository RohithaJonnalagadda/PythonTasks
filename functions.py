# Find the Sum of Two Numbers
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
#  Find the Largest Number
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(15, 10))
# Check Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(25))
# Find the Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))
# Reverse a String
def reverse_string(text):
    return text[::-1]
print(reverse_string("Python"))
#Count Vowels
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))
# Reverse a String
def reverse_string(text):
    return text[::-1]
print(reverse_string("Python"))
# Count Vowels
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count
print(count_vowels("Hello World"))
# Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(17))
# Find the Maximum Element in a List
def maximum(numbers):
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    return max_num
print(maximum([12, 45, 8, 90, 23]))
# Calculate the Average
def average(numbers):
    total = sum(numbers)
    return total / len(numbers)
print(average([10,20,30,40]))
# Check Palindrome
def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(palindrome("madam"))
