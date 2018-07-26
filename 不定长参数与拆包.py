#05-不定长参数
def test(x,y,*args,**kwargs):
    print(x,y)
    print(args)
    print(kwargs)
    num = x+y
    for i in args:
        num += i
    for i in kwargs.values():
        num +=i
    print("和为%s"%num)

test(1,2,3,4,5,a=6,b=7)
num1={"a":1,"b" :2}
c=num1.values()
print(c)

#集合的拆包
nums1=(1,2)
nums2={"a":1,"b":2,"c":3}
test(1,2,*nums1,**nums2)