# 当无法确定代码是否能执行时，可以使用try...except...关键字

# try:
#     num = int(input("please enter an integrate:"))
# except:
#     print("you've enter a wrong number")
#
# print(50*"_")

# 捕获不同类型的错误

try:
    num = int(input("please enter an integrate:"))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除数为0")
# 如果还有位置错误
except Exception as error_result:
    print("%s 未知错误" % error_result)
# 如果没有错误，执行else下方的代码
else:
    print("已输出结果")
# 无论是否发生错误，都执行finally的代码
finally:
    print(50 * "_")


# 异常的传递，在主程序中进行异常捕获即可

def demo1():
    return int(print(input("请输入一个整数")))


def demo2():
    return demo1()


try:
    demo2()
except Exception as result:
    print(("%s 未知错误") % result)
