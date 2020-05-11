#python循环语句
#python两种循环：for循环和while循环
# while循环
# while 条件:
#   执行代码
#不同于其他语言仍然是条件后面有:
#执行代码多行不需要{}通过是否有tab判断
# break and continue
count=0
while count<=100 :
#对于条件后在执行语句不能为空，会报缩进错误，使用pass来代替
    if count==50 :
        #pass#跳过
        #break
        continue #跳出这次循环整个循环体都不会执行，count的值一直是50,所以不会有变化;所以循环变量应该在continue之前
    elif count>=60 and count <=80 :
        print("%s 的平方是：" % count,count**2)
    else :
        print("本身",count)
    count +=1
print ("loop is end")
