# public method for object like list, 元组，string, dict
# for...break...else

for num in [1,2,3]:
    print(num)
    if num == 2:
        break
else:
    print("not 1, 2, 3")


students = [{"name":"xiaoming","age":"18"},{"name":"xiaomei","age":"19"}]

for stu_dict in students:
    
    if stu_dict["name"] == "zhangshan":
        # print("find xiaomei")
        print(stu_dict)
        break
else:
    print("not find in the list")
print("end loop")