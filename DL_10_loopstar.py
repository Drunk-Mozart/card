line = 1

while line <= 5:
    a = 1
    while a <= line:
        print("*", end="")
        a += 1
    print("")
    line += 1

a = 1
while a <= 9:
    b = 1
    while b <= a:
        cal = a * b
        print("%d * %d = %d"%(b, a, cal), end = "\t")
        b += 1
    print("")
    a += 1

def multi_cheng():
    a = 1
    while a <= 9:
        b = 1
        while b <= a:
            cal = a * b
            print("%d * %d = %d"%(b, a, cal), end = "\t")
            b += 1
        print("")
        a += 1