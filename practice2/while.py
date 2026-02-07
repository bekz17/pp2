i = 1
while i < 6:
    print(i)
    i += 1

j = 0
while j < 3:
    print(j)
    j += 1

k = 5
while k > 0:
    print(k)
    k -= 1

x = 2
while x <= 6:
    print(x)
    x += 2

y = 10
while y > 5:
    print(y)
    y -= 1


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

j = 0
while j < 5:
    if j == 2:
        break
    print(j)
    j += 1

k = 1
while k <= 10:
    if k > 7:
        break
    print(k)
    k += 2

x = 1
while x < 6:
    x += 1
    if x == 4:
        break
    print(x)

y = 0
while y < 10:
    if y % 3 == 0 and y != 0:
        break
    print(y)
    y += 1


i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

j = 0
while j < 5:
    j += 1
    if j == 2:
        continue
    print(j)

k = 1
while k <= 10:
    k += 1
    if k % 2 == 0:
        continue
    print(k)

x = 0
while x < 7:
    x += 1
    if x == 5:
        continue
    print(x)

y = 1
while y < 6:
    if y == 4:
        y += 1
        continue
    print(y)
    y += 1
