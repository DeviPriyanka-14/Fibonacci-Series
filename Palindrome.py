num = input("Enter a number: ") 
reverse_num = num[::-1] 
if num == reverse_num:
    print("Palindrome")
else:
    print("Not a palindrome")
