"""
Sum of Digits.
Example:
Input: 12345
Output: 5+4+3+2+1
"""
num = input("Enter a number: ")

result = 0
for digit in num:
    result += int(digit)

print("The sum of the digits is:", result)
