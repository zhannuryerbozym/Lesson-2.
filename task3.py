z= int(input("neshege deyin"))
x=1
while x <=9:
    y=1
    while y<=9:
        print(x, "*", y, "=", x*y)
        y=y+1
    print("")
    if x==z:
        break

    x=x+1
