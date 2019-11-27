def dayin():
    print("*" * 50)


def dayin2():
    print("-" * 50)
    dayin()
    print("+" * 50)


dayin2()


def dayin3(char, times):
    print(char * times)


dayin3("^", 50)


def mul_print(char, times, n):
    """

    :param char:
    :param times:
    :param n:
    """
    i = 1

    while i <= n:

        dayin3(char, times)

        i += 1


mul_print("-", 50, 5)

