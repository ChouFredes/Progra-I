def ackermann(m,n):
    if m==0:
        return n+1
    elif n==0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))

for i in range(0,3):
    print()
    for x in range(0,7):
        print(ackermann(i,x), end=",")

