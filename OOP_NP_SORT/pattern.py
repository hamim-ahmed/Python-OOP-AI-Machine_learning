n = int(input("Enter a number:"))
x = n           #middle position 1
y = n + 1       #middle position 2
for i in range(1, n*2+1):
    print("*", end =" ")
print()
for j in range(n):                     #for n number of rows.
    for i in range(1,n*2+1):           #for n*2 stars in each rows.
        if i in range(x,y+1):          #middle positions get replaced by space in every rows.
            print(" ", end=" ")
            continue
        else:
            print("*", end=" ")
    if j < n-2:                     #print a new line until the last iteration.
        print()
    x=x-1
    y=y+1

x=1
y=n*2
for j in range(n):
    for i in range(1,n*2+1):
        if i in range(x,y+1):
            print(" ",end=" ")
            continue
        else:
            print("*", end=" ")
    print()
    x=x+1
    y=y-1
for i in range(1, n*2+1):
    print("*", end =" ")
print()
