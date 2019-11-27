

def print_line(char, times):
    """
print line
    :param char: fuhao
    :param times:  cishu
    """
    print(char * times)


def mul_print(char, times, n):
    """
print multi lines
    :param char: zifu
    :param times: cishu
    :param n: hangsu
    """
    i = 1

    while i <= n:

        print_line(char, times)

        i += 1


name = "dragon"