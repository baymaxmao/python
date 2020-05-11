#格式化输出
name=input("Name:")
age=input("Age:")
job=input("Job:")
hometown=input("Hometown:")
#print("---------info of",name,"----")
#print("Name:",name)
#print("Age:",age)
#print("Job:",job)
#print("---------end-------")


#使用占位符定义输出格式
info="""
----------info of %s ------
Name:       %s
Age:        %s
Job:        %s
Hometown:   %s
------------end------------
""" % (name,name,age,job,hometown)
print(info)
