"""
Get String From User and Count All Words in the String
Example:
Input: alpha
Output: 
a: 2
l: 1
p: 1
h: 1
"""
txt = input("Enter a string: ")
count = {}
for i in txt:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for key, value in count.items():
    print(f"{key}: {value}")
