a = "broadway"
b = "infosys"
#operations
print(a+b)#combines the subjects
str1= "hello world"
x=slice(2,5)#slicing
#python string ,ethods
d=str1.capitalize()#capitalizes the first letter
print(d)
e=str1.upper()#capitalizes all the word to the uppercase
print(e)
f=str1.lower()# turns every word to lower case
print(f)
g=str1.title()# capitalizes the first letter in every word
print(g)
str1="cookie cutter"
str2="Cut"
str3="cut"
h=str1.find(str2)#finding cut(str2) in cookie cutter(str1)
print(h)
i=str1.find(str3)
print(1)# if it cannot find cut in str1 then the result is always -1, Cut and cut is not the same
str4="hip hip hurray"
j=str4.replace('hip','Hip')#replacement
print(j)
k=j.replace('Hip','hip',1 )
print(k)
s = "hello world"
r = s.split()#splits the words from the part given in the bracket
print(r)
#string formatting
message = f"i study at {a}"#{} brings the input value of the given word
print(message)
print('i am {} and i am {} years old.'.format('john doe',23))#another way of formatting
print('{a}, {b}, {c}'.format(a='foo', b='bar', c='baz'))#formatting
t = "john wick"
#use of f string
print(f"hi! {t}")#brings the value of t
print(f"{{2+3}}")#double curly brackets prints the given input and doesnot operate but
print(f"{2+3}")#operates the function and gives the output


