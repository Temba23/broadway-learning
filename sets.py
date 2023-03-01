#python sets dont have order
#sets are mutable and elements cant be mutable
#dictionary cant be inputed but tuple can be.
s1 = {1,2,3}
(s1.add(4))# adds the number 4 in the set s1
print(s1)
t1 = {1, 2, 3, 4}
t1.discard(4)#deletes the value 4 from the set t1 and it gives null value if something not in the set is given.
print(t1)
u1 = {1, 2, 3, 4}
u1.remove(4)#deletes the value from the set and it gives error if something unavailable is given.
print(u1)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))#it gives the intersection between the two sets
print(a.union(b))#it gives the union of the two sets
print(a.difference(b))#it gives the values available in set a which are not present in set b
print(a.symmetric_difference(b))#it gives the values that are only available in a and b
# conditions and loops
# we write elif
# elif statement is checked even if the condition if is true but it is not checked in the else statement
# a = int(input("enter the first number"))
# b = int(input("enter the second number"))
# c = int(input("enter the third number"))
# if a > b and a > c:
#     print(f"{a} is the greatest")#f"{a} gives the number inside or value of a
# if b > c and b > a:
#     print(f"{b} is the greatest")
# if  c > a and c > b:
#     print(f"{c} is the greatest")

# Looping
for i in range(10): # it ranges from 0-9
    print(i)
for i in range (1, 11 ):
    print(i)

# find the even numbers from the first 10 natural numbers.
for i in range(1,11):
    if i%2==0:
        print(i)

#for the first thirty numbers print the number as it is, if otherwise divisible by 3 print ' fizz ' , if divisible by 5
    #print 'buzz' , if divisible by both 3 and 5 print 'fizzbuzz'***
for i in range(31):
    if i % 3 and i % 5 == 0:
        print("fizzbuzz", end = "")
        break#the loop stops after the condition is met and no further looping is done
    elif i % 5 == 0:
        print("fizz", end = "")
    elif i % 3 == 0:
        print("Buzz", end = "")
    else:
        print(i, end = "")

for x in [1,2,'a']:
    print(x)
# git clone and alink of the file helps to open the new project which already exists.
# git stash temporarily cuts the new data and git stash apply paste it.
# d.keys gives the key value from the dictionary.
# d.values give the values from the dictionary

d= {
    "name" : "abc",
    "age" : "12",
    }
print(d.keys())
#for key in d.keys:
# print(key)
#for values in the d.values():
# print(values)
for key, values in d.items():
    print(key,values())

 #range(1, 10) #0-9
#range(1, 10, 2) #gives in the jump of 2
a = [1, 2, 3, 4]
for index, value in enumerate(a):
    print(i)
    


















