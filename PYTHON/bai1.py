print("Hello word")
# Syntax lui dau dong
if 5 > 2:
 print("canh dep trai")
#Variables
x = 5
y = "John"
print(x)
print(y)
#DATA TYPE
x = 5
print(type(x))
#NUMBER
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1,4))
#Casting = convert
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)
# String
a  = "canh" 
print(a)
a = "hello, World"
print(a[1])

print(a[2:5])
print(len(a))

txt = "The best things in life are free!"
if "free" not in txt:
  print("Yes, 'free' is present.")
#  BOOLEANS
print(1 > 2)

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

X = 200
Y = 4
if X > Y:
 print('canh dung')
else:
 print('canh sai')
 

#Operators
print((4+5) +(5+1))
#LIST
listcanh = ["canh","thuy","anh"]
print(listcanh)
print(listcanh[1:3])
print(listcanh[0:])
#tuple thay doi 
thistuple = ("canh","thuy","nghia")
print(thistuple)
#SET
thisset = {"canh","thuy","nghia"}
print(thisset)
#dictionaries
thisdict = {
"nghia": "canh",
"thuy" : "anh"
}
print(thisdict["nghia"])
# if else
a = 3
b = 4
if a >b:
  print("ok")
elif a == b:
  print("ko")
else:
  print("not ok")
# while loops
i = 1
while i < 9:
  print(i)
  i +=2

i = 1
while i < 9:
  print(i)
  i +=2
  if i == 5:
    break
  i +=1

# for loops
canh = ["c", "b", "c"]
for x in canh:
  print(x)

canh = ["a", "b", "c"]
for x in canh:
  print(x)
  if x == "b":
    break
#Function 
def my_function(x):
  print(x +"canh dep trai")
my_function  

def function(nhap):

  print(nhap + " so")
function("1")
function("2") 
#lambda
x = lambda a : a + 10
print(x(5))

def myfunc(n):
  return lambda a : a * n

ket_qua = myfunc(2)

print(ket_qua(11))
#Arrays
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)
