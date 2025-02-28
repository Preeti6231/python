#write A python program to accept a number and print wheater it is
#1 digit, 2 digit , 3 digit or more than 3 digit number.

num = int(input("Enter any Number"))
if num>=1 and num<=9:
    print("1 digit Number")
else :
    if num>=10 and num<=99:
        print("2 digit Number")
    else :
        if num>=100 and num<= 999:
            print("3 digit Number")
        else :
            print("More than 3 digit")
