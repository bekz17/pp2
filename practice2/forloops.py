fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)

letters = ["a", "b", "c"]
for l in letters:
    print(l)

mixed = ["apple", 10, True]
for item in mixed:
    print(item)

word = "Python"
for letter in word:
    print(letter)


for x in "banana":
    print(x)

word = "Python"
for letter in word:
    print(letter)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

letters = ["a", "b", "c", "d"]
for l in letters:
    print(l)

mixed = ["apple", 10, True]
for item in mixed:
    print(item)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 4:
        break
    print(n)

letters = ["a", "b", "c", "d"]
for l in letters:
    if l == "c":
        break
    print(l)

mixed = ["apple", 10, True, "banana"]
for item in mixed:
    if item == True:
        break
    print(item)

word = "Python"
for letter in word:
    if letter == "h":
        break
    print(letter)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        continue
    print(n)

letters = ["a", "b", "c", "d"]
for l in letters:
    if l == "c":
        continue
    print(l)

mixed = ["apple", 10, True, "banana"]
for item in mixed:
    if item == 10:
        continue
    print(item)

word = "Python"
for letter in word:
    if letter in "aeiou":
        continue
    print(letter)
