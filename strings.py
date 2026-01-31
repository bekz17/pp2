#slicing
# --- Slicing: getting a part of the string ---
b = "Hello, World!"

# Get characters from position 2 to 5 (not included)
print(b[2:5])  # "llo"

# Slice from the start to position 5 (not included)
print(b[:5])   # "Hello"

# Slice from position 2 to the end
print(b[2:])   # "llo, World!"

# Negative indexing: from -5 to -2
print(b[-5:-2])  # "orl"

# Another slicing example
# Get characters from 0 to 8
print(b[0:8])   # "Hello, W"

# Slice with step
# Get every 2nd character from position 0 to 10
print(b[0:10:2])  # "Hlo o"

# Slice the whole string
print(b[:])     # "Hello, World!"

# Slice using negative step (reversing the string)
print(b[::-1])  # "!dlroW ,olleH"

# Slice with start omitted and step 2
print(b[::2])   # "Hlo ol!"

# Slice last 5 characters
print(b[-5:])   # "orld!"
#Modify strings
# --- Upper Case ---
a = "Hello, World!"
print(a.upper())  # "HELLO, WORLD!"

# --- Lower Case ---
a = "Hello, World!"
print(a.lower())  # "hello, world!"

# --- Remove Whitespace ---
a = "   Hello, World!   "
print(a.strip())  # "Hello, World!"

# --- Replace String ---
a = "Hello, World!"
print(a.replace("H", "J"))  # "Jello, World!"
print(a.replace("World", "Python"))  # "Hello, Python!"

# --- Split String ---
a = "Hello, World!"
print(a.split(","))  # ['Hello', ' World!']
b = "apple,banana,cherry"
print(b.split(","))  # ['apple', 'banana', 'cherry']

# --- Basic Concatenation ---
a = "Hello"
b = "World"
c = a + b
print(c)  # "HelloWorld"

# --- Concatenation with Space ---
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # "Hello World"

# --- Concatenate multiple strings ---
a = "Python"
b = "is"
c = "fun"
d = a + " " + b + " " + c
print(d)  # "Python is fun"

# --- Basic f-string ---
age = 36
txt = f"My name is John, I am {age}"
print(txt)  # "My name is John, I am 36"

# --- Placeholder with a variable ---
price = 59
txt = f"The price is {price} dollars"
print(txt)  # "The price is 59 dollars"

# --- Placeholder with a math operation ---
txt = f"The price is {20 * 59} dollars"
print(txt)  # "The price is 1180 dollars"

# --- Multiple variables in f-string ---
name = "Alice"
age = 25
txt = f"My name is {name} and I am {age} years old"
print(txt)  # "My name is Alice and I am 25 years old"

# --- Using escape character for quotes ---
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
# Output: We are the so-called "Vikings" from the north.

# --- Single quote inside single-quoted string ---
txt = 'It\'s a beautiful day'
print(txt)
# Output: It's a beautiful day

# --- Backslash itself ---
txt = "This is a backslash: \\"
print(txt)
# Output: This is a backslash: \

# --- New Line ---
txt = "Hello\nWorld!"
print(txt)
# Output:
# Hello
# World!

