#允许用户最多猜3次，中间猜对国结束
age=26 
count=0
while count <3:
    guess_age=int(input("Please enter the age"))
    if guess_age==age:
        print("You got")
        break
    elif guess_age>age :
        print("smaller")
    else :
        print("bigger")
    count+=1

