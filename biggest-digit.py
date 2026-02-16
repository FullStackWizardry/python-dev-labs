"""
Return Biggest Digit in a Number 
Example:
Input: 12345
Output: 5
"""
num = input("Enter a number: ")

result = 0
for digit in num:
    if int(digit) > result:
        result = int(digit)

print("The biggest digit is:", result)
