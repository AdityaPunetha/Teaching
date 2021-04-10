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
friends.clear()
friends.pop()
print(friends.index("adi"))
print(friends.count("adi"))
friends.sort()
a = sorted(friends)
friends.reverse()
friends2 = friends.copy()
'''Tuples'''
numbers = (2, 3)
numbers[1] = 7
numbers = [(2, 3), (4, 5), (3, 6)]
'''Functions'''


def say_hi():
    print("Hi")


say_hi()


def sayhi(name, age):
    print("Hi " + name + " " + age)


sayhi("ADitty]", 88)
'''return'''


def cube(x):
    return x ^ 3


print(cube(4))
result = cube(3)
print(result)
'''If'''
is_male = True
if is_male:
    print("You are a male")
else:
    print("not male")
tall = True
if is_male or tall:
    print("male or tall")

if is_male and tall:
    print("male and tall")
elif is_male and not tall:
    print("male n not tall")
elif not is_male and tall:
    print("tall girl")
else:
    print("short girl")

'''if comparisons'''


def maxno(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    else:
        return c


print(maxno(1, 3, 5))
if "abc" == "abc":
    pass
'''dict'''
months = {
    "jan": "january", "feb": "february", "mar": "march"
}
print(months["feb"])
print(months.get("mar"))
print(months.get("monday", "not valid"))
months = {
    1: "january", 2: "february", 3: "march"
}
'''while'''
'''For'''
for letters in "aditya":
    print(letters)
