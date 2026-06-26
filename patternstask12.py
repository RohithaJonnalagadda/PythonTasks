num =153
temp = num
length = len(str(num))
sum = 0
while temp > 0:
    digit = temp % 10
    sum +=digit ** length
    temp //=10
if sum==num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")