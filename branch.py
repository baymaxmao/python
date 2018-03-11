#流程控制
#单分支
#if 条件：
#   执行代码
####不同于其他语言条件后面跟: 一般代码规范 tab
age=18
if age<18 :
    print("You are a child")
print("I don't know")
    
#双分支
#if 条件：
#else :
_username="maoshanli"
_password="msl"

username=input("please enter your name")
password=input("please enter your password")
if _username==username and _password==password :
    print('welcome %s' % username)
else :
    print("account is error")

