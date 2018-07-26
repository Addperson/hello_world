#copy文件

#两个文件的位置，把其他位置位置copy到另一位置，下面列子中位置相同
source_file="E:\python\文件操作\\text.txt"
dest_file="copy-"+source_file[source_file.rfind("\\")+1:]

#打开和建立文件
source=open(source_file,"r")
dest  =open(dest_file,"w")

#从原先文件读取，写入新文件
content=source.read()
dest.write(content)

#关闭文件
source.close()
dest.close()