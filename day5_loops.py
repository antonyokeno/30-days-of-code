
num = int(input("Enter num: "))
if num>=2 and num<=20:
    for i in range(1,11):
        print (num,'x',i,'=',num*i)
else:
    print("number out of range")
