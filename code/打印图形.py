h=int(input("菱形高度="))
for i in range(h//2+1):  #top
    for j in range(1,h+1):
        if(j<(h+1)//2-i or j>(h+1)//2+i):
            print(" ",end="")
        else:
            print("*",end="")
    print("")
for i in range(h//2):
    for j in range(1,h+1):
        if (j < i+2 or j > (h + 1) -i-2):
            print(" ", end="")
        else:
            print("*", end="")
    print("")