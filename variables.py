# 1. Simple variables
x = 10
y = 20
print(x)
print(y)

# 2. Changing variable type
num = 100
num = "One hundred"
print(num)

# 3. Casting variables
a = str(25)    # becomes string '25'
b = int("15")  # becomes integer 15
c = float(7)   # becomes float 7.0
print(a, b, c)

# 4. Getting the type
x = 3.14
y = "Python"
z = True
print(type(x))
print(type(y))
print(type(z))

# 5. Using single and double quotes
name1 = 'Alice'
name2 = "Bob"
print(name1, name2)

# 6. Case-sensitive variable names
fruit = "Apple"
Fruit = "Banana"
fRuIt = "Cherry"
print(fruit)
print(Fruit)
print(fRuIt)

# 7. Multiple assignments in one line
a, b, c = 1, 2, 3
print(a, b, c)

# 8. Assigning the same value to multiple variables
x = y = z = "Hello"
print(x, y, z)

# 9. Variables with numbers in names
score1 = 50
score2 = 75
print(score1 + score2)

# 10. Variable with mixed types
val = 10
val = "Ten"
print(val)
#assign multiple values
# Original example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# 1. Unpacking numbers
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)

# 2. Unpacking strings
names = ["Alice", "Bob", "Charlie"]
n1, n2, n3 = names
print(n1, n2, n3)

# 3. Unpacking mixed types
data = [10, "Hello", 3.14]
num, text, pi = data
print(num, text, pi)

# 4. Unpacking booleans
flags = [True, False, True]
f1, f2, f3 = flags
print(f1, f2, f3)

# 5. Unpacking with different variable names
colors = ["red", "green", "blue"]
r, g, b = colors
print(r, g, b)

# 6. Unpacking more elements
items = ["pen", "pencil", "eraser", "sharpener"]
i1, i2, i3, i4 = items
print(i1, i2, i3, i4)
