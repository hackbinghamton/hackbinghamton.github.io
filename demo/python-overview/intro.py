# Hello world
print('Hello, world!')


# Indentation is important in Python!
x = 1
if x == 1:
    print('x is 1')


# Numbers and Strings
my_int = 8
print(my_int)

my_float = 1.4
print(my_float)

a, b, c = 1, 2, 3
print(a, b, c)


my_string = 'hello'
print(my_string)

my_string = "hello"
print(my_string)


# Operators
one = 1
two = 2
three = one + two

print(one < two)
print(one > two)
print(two > one)
print(three == 3)

helloworld = 'hello' + ' ' + 'world'
print(helloworld)

print(one + helloworld)


# Lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist)
print(mylist[0])
print(mylist[1])
print(mylist[2])

print(mylist[3]) # IndexError

print(len(mylist))

print(0 in mylist)
print(4 not in mylist)

x, y, z = mylist
print(x)
print(y)
print(z)


# Looping over lists
for item in mylist:
    print(item)

mylist = [1, "Alice", True, ['Bill']]


# More Operators
print(7 + 3.0)      # addition
print(2 ** 3)       # exponents
print(3 - 4)        # subtraction
print(3 / 2)        # division
print(3 // 2)       # integer division
print(14 % 12)      # remainder. like clock arithmetic

# Operators on Strings
print('hello' + ' ' + 'world')   # concatenation
print('hello'*5)                 # repeat

# Operators on Lists
print([1, 2, 3] + [7, 8, 9])
print([1, 2, 3] * 3)

# Formatting Strings
answer = 42
print(f'the answer is {number}')

# Dictionary
ages = {'alice': 23, 'bob': 12, 'frank': 66}
print(ages['alice'])
ages[3] = True
print(ages)
ages['bob'] += 1
print(ages)


# Functions
def square(x):
    return x ** 2

print(square(2))

def say_hello():
    print('hello')

x = say_hello()
print(x)

def square_multiple(a, b, c):
    return a ** 2, b ** 2, c ** 2

result = square_multiple(1, 2, 3)
print(result)
x, y, z = result

# Looping
x = 10
while x > 0:
    print(x)
    x -= 1
