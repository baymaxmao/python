#python 特有在语句while ...esle语句，如果循环不中断，就执行else部分的语句
#whle结束之后会有语句为什么需要else，实际作用是什么？？
# 用于调试，判断循环程序是否被中断，若被中断了就执行一些其他操作，类似于系统中断。
count=0
while count<=5 :
    print(count)
    count+=1
else :
    print("the loop is end")
print ("out")
