def armstrog(number):
    sum=0
    length=len(number)
    while(number>0):
        rem=number%10
        sum+=rem**length
        number=number//10
    return sum
number=153 #int(input("enter the number:"))
res_sum=armstrog(number)
if(res_sum==number):
    print("armstong")
else:
    print("not armstong")