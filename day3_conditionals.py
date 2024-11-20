n = int(input().strip())
if n>=1 and n<=100:
    if n%2==0:
        if n<5:
            print("Not Weird.")
        elif n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird.")
    else:
        print("Weird")
else:
    print("Invalid inputs, try again")

