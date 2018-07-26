def print_menu():
    print("*"*30)
    print("学生管理系统".center(50))
    print("输入1:添加学生")
    print("输入2:查找学生")
    print("输入3:删除学生")
    print("输入4:修改学生")
    print("输入5:查看所有学生")
    print("输入6:退出")
def copy_student(i):
    print("姓名：%s,性别：%s,年龄：%s,"%(i["name"],i["sex"],i["age"]))
def add_student():
    name=input("输入姓名：")
    sex =input("输入性别：")
    age =input("输入年龄：")
    stu ={"name":name,"sex":sex,"age":age}
    stus.append(stu.copy())

    #这里用字典的.copy函数的作用是什么，不加这个函数报错：字符串类型应该为int，比如a[0]
    #系统把字典当成list对待，为什么??


    print("添加成功")
def del_student():
    name=input("想要删除的学生姓名：")
    for i in stus:
        if i["name"] == name:
            stus.remove(i)
def find_student():
    name =input("查找的学生姓名：")
    for i in stus:
        if i["name"] == name.strip():
            copy_student(i)
            break
    else:
        print("查无此人！")
def copy_allstudent():
    for i in stus:
        copy_student(i)



def main():
    print_menu()
    while True:
        i=input("输入你想要的操作：")
        if  i == "1":
            add_student()#添加学生
        elif  i == "2":
            find_student()#查找学生并打印
        elif  i == "3":
            del_student()#删除学生
        elif  i == "4":
            pass
        elif  i == "5":
            copy_allstudent()#打印所有学生
        elif  i == "6":
            break

stus=[]
main()