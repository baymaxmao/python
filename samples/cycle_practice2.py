#允许用户最多输3次，猜了3次后，再问是否还想玩，如果用户选择y,再允许三次，以此往复
count=1
age=26
while True:
    print(count,count%4)
    if count%4==0:
        print("continue or not,if you want to continue,please enter y else enter n")
        con=input("please enter y or n:")
        if con=="n" :
            break
        else :
            count+=1
            continue

    else :
        guess_age=int(input("please enter your guess:")) 
        if guess_age==age:
            print("you got")
        elif guess_age>age :
            print("smaller")
        else:
            print("bigger")
    count+=1
     
