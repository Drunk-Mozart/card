i = 0
summary = 0
while 100 >= i:
    summary += i
    i += 1
print(summary, i)

i = 0
summary = 0
while 100 >= i:
    summary += i
    i += 2
    if i == 2:
        break
    print(i)
print(summary, i)

i = 0
result = 0
while i <= 100:
    i += 1
    if i % 2 == 1:
        continue
    print(i)
    result += i
print(result)


