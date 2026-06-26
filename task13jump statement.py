#1. Square Pattern 
for i in range(4):      
    for j in range(4):  
        print("*", end=" ")
    print()

 #2. Right Triangle
 for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

#Number Triangle 
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Repeated Number Triangle 
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

# Alphabet Triangle
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# Inverted Star Triangle
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# 8. Continuous Number Pattern
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#Right aligned
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()

#Pyramid Pattern
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()




