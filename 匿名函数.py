'''匿名函数
def test(a,b,func):
    result=func(a,b)
    return result
print(test(10,20,lambda x,y:x+y))
'''

#匿名函数用于排序
stus=[{"name":"zs","age":22},{"name":"ls","age":33},{"name":"ww","age":18}]
#key值表示sort按照什么排序，默认为key=none没有指定，此时按照元素本身排序
stus.sort(key=lambda x:x["age"])#此句话中匿名函数返回列表元素（字典）中age的值用于排序，也可修改为name
print(stus)

def test(a,b,func):
    result=func(a,b)
    return result

func_new=input("你想要的操作：")
func_new=eval(func_new)#input默认输入结果为字符串，此语句把字符串转化为表达式
print(test(10,20,func_new))