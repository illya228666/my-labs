N = int(input("enter the value N "))
while (N<1 or N>9):
    print("value N is incorrect")
    N = int(input("enter the value N "))
for i in range(N+1):
    for w in range(6-i):
        print(w)
