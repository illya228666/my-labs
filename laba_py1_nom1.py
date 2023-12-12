while True:
    a = int(input("enter the value a "))
    b = int(input("enter the value b "))
    if a<=0:
        print("the value a is incorrect, a should be greater than 0")
        a = int(input("enter the value a "))
    if b<=0:
        print("the value b is incorrect, b should be greater than 0")
        a = int(input("enter the value b "))
    if a<b:
        x=a/b+1
    elif a==b:
        x=-1
    else:
        x = (a*b-5)/a
    x = round(x, 2)
    print("x=", x)
