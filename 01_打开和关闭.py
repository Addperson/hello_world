#打开和关闭

f=open("text.txt","r+")
f.write("hello\tworld")
content=f.read(5)
print(content)
f.close()


