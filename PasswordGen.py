import random
import subprocess

def copy(x):
    cmd='echo '+x.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #1 (26)
lower = upper.lower() #2 (26)
numbers = "0123456789" #3 (10)
special = "!@#$%^&*():;'\"<>?/\\.,`~" #4 (25)
password = ""

print("Difficulty: ")
print("0: LOW  (Only nums)")
print("1: MED  (Only letters)")
print("2: HIGH (Letters+Nums)")
print("3: EXTR (Everything)")

while True:
    try:
        global ValType
        ValType = int(input())
    except ValueError:
        print("Please give a number")
    else:
        break

print("Length: ")

def generateRandomInt(x, y):
    return random.randint(x, y)
    
while True:
    try:
        global length
        length = int(input())
    except ValueError:
        print("Please give a number")
    else:
        break

if ValType == 0: #LOW
    for x in range(length):
        password += numbers[generateRandomInt(0, 9)]

elif ValType == 1: #MED
    for x in range (length):
        num = generateRandomInt(0, 1)
        if num > 0:
            password += lower[generateRandomInt(0, 25)]
        else:
            password += upper[generateRandomInt(0, 25)]
elif ValType == 2: #HIGH
    for x in range (length): 
        num = generateRandomInt(0, 3)
        if num == 0:
            password += lower[generateRandomInt(0, 25)]
        elif num == 1:
            password += numbers[generateRandomInt(0, 9)]
        else:
            password += upper[generateRandomInt(0, 25)]
elif ValType == 3: #EXTR
    for x in range (length): 
        num = generateRandomInt(0, 4)
        if num == 0:
            password += lower[generateRandomInt(0, 25)]
        elif num == 1:
            password += numbers[generateRandomInt(0, 9)]
        elif num == 2:
            password += upper[generateRandomInt(0, 25)]
        else:
            password += special[generateRandomInt(0, 24)]
else:
    print("Error")

print(password)
copy(password)
input()


    


