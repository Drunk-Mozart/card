# 这种方法只能打开英文文件
# 先open，直接调用关闭，否则会浪费很多系统资源

file = open("txt_sample")

text = file.read()
print(text)
print(50*"_")

# read 将文件指针移到末尾，无法再次read
text = file.read()
print(text)


file.close()

# 在open函数，加入r，w，a参数，对文件进行读，写，添加的操作
# file1 = open("txt_sample", "a")
# file1.write("hello")
# file1.close()

# 逐行读取
file1 = open("txt_sample", "r")

while True:
    text = file1.readline()
    if not text: # text is none是无法跳出循环的
        break
    print(text)

file1.close()