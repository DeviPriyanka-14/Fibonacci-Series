num = int(input("Enter a number: "))
sum = 0
temp = num
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10
if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
