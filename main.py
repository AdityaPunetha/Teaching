print("hello world")
'''data and variables'''
name = "Aditya"
age = 778.2344
print("my name is aditya")
print("i am 18 years old")
a = True
"""Strings"""
print("aditya\n punetha")
print("aditya\" punetha")
word = "Aditya Punetha"
print(word)
print(word + "is a कूल डूड ")
print(word.lower())
print(word.islower())
print(word.upper().isupper())
print(len(word))
print(word[3])
print(word.index("t"))
print(word.index("a"))
print(word.index("Pun"))
print(word.replace("Punetha", "Singh"))
"""Numbers"""
print(2)
print(2.5)
print(2 + 3)
print(3 ** 3.5)
print(3 * (4 + 5))
num = 5
print(str(num))
print(max(2, 3))
print(min(2, 3))
import math

print(math.floor(4.6))
print(math.ceil(4.6))
print(math.sqrt(81))
"""Input"""
input()
input("Enter your name: ")
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + " ! You are " + age + " years old!")
"Basic Calc"
num1 = input("Enter a no.: ")
num2 = input("Enter 2nd no.: ")
result = num1 + num2
print(result)
'''Lists'''
friends = ["Aditya", "Dhanraj", "Medhavi", "Rohan", "Sid"]
list = ["Punetha", 2, True]
print(list)
print(*list)
print(list[1])
print(list[-1])
print(list[1:])
friends[1] = "hello"
fav_no = [2, 3, 1, 46, 6]
friends.extend(fav_no)
friends.append("world")
friends.insert(1, "adi")
friends.remove("Sid")
