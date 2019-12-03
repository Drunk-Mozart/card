def input_usr():
    pwd = input("please input your password:")
    if len(pwd) >= 8:
        return pwd
    ex = Exception("密码长度小于8位")
    raise ex

try:
    print(input_usr())
except Exception as result:
    print(result)
