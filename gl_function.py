def demo(num, num_list):
    # 全局变量将引用传入函数，函数形参改变引用，不改变全局变量引用
    num = 99
    num_list = [1, 2, 3]
    print(num)
    print(num_list)


gl_num = 100
gl_num_list = [4, 5, 6]
demo(gl_num, gl_num)
print(gl_num)
print(gl_num_list)

# 交换两个变量的值
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)


# def demo2(num_list):
#     # 实参传入，内部方法改变变量，全局变量改变
#     num_list.append(9)
#     print(num_list)
#
#
# demo2(gl_num_list)
# print(gl_num_list)


def demo3(num, num_list):
    num += num
    num_list += num_list  # 本质上在调用Extend方法，如果只用+就不会影响全局变量指向的列表
    print(num)
    print(num_list)


demo3(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)

gl_num_list.sort(reverse=True)  # 函数缺省值，为false，若不指定则为默认值
print(gl_num_list)


# TODO set for any todo list


def demo4(name, gender=True):
    """
    设置缺省参数
    :param name: 姓名
    :param gender: 性别 True=男生
    """
    # 缺省参数必须在末尾
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


demo4("小明")
demo4("小美", 0)


def demo5(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo5(1, 2, 3, 4, name="小明", age=18)


def sum_num(*args):
    num = 0
    for i in args:
        num += i
    print(num)


sum_num(1, 2, 3, 4, 5)


def demo6(*args,**kwargs):
    print(args)
    print(kwargs)


gl_dict = {"name":"小明", "age":18}
demo6(gl_num_list,gl_dict)
demo6(*gl_num_list,**gl_dict)