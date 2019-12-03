# 导入模块：import
# 给导入的模块起别名：import...as...，
# 导入模块中的某个工具：from module import...；如果导入两个模块有相同的函数，则后导入会覆盖先导入
# 模块导入最好都写在顶部，容易发现同名函数，可以通过给函数起别名的方式实现同名区分
# 没有缩进的代码，都会在导入模块时被执行

import random


def main():
    print(random.__file__)
    rand = random.randint(1, 10)
    print(rand)


if __name__ == "__main__": # 如果导入此模块，__name__将不再是__main__，可以保证下方代码不在导入后执行
    main()
    print(__name__)