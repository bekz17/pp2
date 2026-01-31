# --- Numeric types assignment ---
x = 1       # int
y = 2.8     # float
z = 1j      # complex

print(x, type(x))
print(y, type(y))
print(z, type(z))


# --- Integers ---
x = 1
y = 35656222554887711
z = -3255522

print(x, type(x))
print(y, type(y))
print(z, type(z))


# --- Floats ---
x = 1.10
y = 1.0
z = -35.59

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Floats in scientific notation
x = 35e3
y = 12E4
z = -87.7e100

print(x, type(x))
print(y, type(y))
print(z, type(z))


# --- Complex numbers ---
x = 3+5j
y = 5j
z = -5j

print(x, type(x))
print(y, type(y))
print(z, type(z))


# --- Type Conversion ---
x = 1       # int
y = 2.8     # float
z = 1j      # complex

# Convert int to float
a = float(x)
# Convert float to int
b = int(y)
# Convert int to complex
c = complex(x)

print(a, type(a))
print(b, type(b))
print(c, type(c))


# --- Random numbers ---
import random

# random number from 1 to 9
rand_num = random.randrange(1, 10)
print("Random number between 1 and 9:", rand_num)