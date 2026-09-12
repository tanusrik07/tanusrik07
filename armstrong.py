a = int(input("Enter a number: "))
num =str(a)
sum = 0
for i in num:
    snum = int(i)
    sum+=snum**2
if sum == a:
    print(a,"is an Armstrong number")
else:
    print(a,"is not an Armstrong number")