import math

counter = 0
while counter < 5:
    print(counter)
    counter += 1

# break helps to stop the program after the condition is met but continue still continues to execute the program aftef
#the condition is met and pass helps to skip the process which makes the code run.

#write a python program to calculate the distance between the points (x1,y1) and (x2,y2).
x1 = int(input("enter the value of x1"))
x2 = int(input("enter the value of x2"))
y1 = int(input("enter the value of y1"))
y2 = int(input("enter the value of y2"))
distance =int((x2 - x1) ** 2 + (y2 - y1)** 2)**1/2
print(distance)
# write a python program to test whether a passed letter is vowel or not
vowel=("a","e", "i","o","u")
a = input("enter the word")
if a in vowel:
    print("a is a vowel letter.")
else:
    print("a is a consonant letter.")
#write a python program to sum two given integers. however, if the sum is between 15 and 20 it will print 20.
c = int(input("enter the first number"))
d = int(input("enter the second number"))
summ = c + d

if summ in range(16, 20):
    print(20)
else:
    print(summ)



