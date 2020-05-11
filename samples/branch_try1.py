score=int(input("Please enter the score(0~100):"))
if score>100 :
   print("Please try again,the score should between 0 and 100")
   score=int(input())
elif score >=90 :
    print ("A")
elif score >=80 :
    print("B")
elif score>=70 :
    print("C")
elif score>=60 :
    print("D")
elif score>=0 :
    print("E")
else :
    print("The score should be between 0 and 100")

