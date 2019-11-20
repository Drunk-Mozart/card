def list_number(num):
    print(num)
    if num == 0:
        return
    list_number(num - 1)


list_number(3)


def sum_number(num):
    if num == 1:
        return 1
    temp_number = sum_number(num - 1)
    return num + temp_number


result = sum_number(3)
print(result)
