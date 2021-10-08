def swapData():
    f1 = input("enter file Name:     ")
    f2 = input("enter file Name2:     ")

    with open(f1,"r") as a:
        data1 = a.read()

    with open(f2,"r") as b:
        data2 = b.read()    

    with open(f1,"w") as a1:
        a1.write(data2)

    with open(f2,"w") as b1:
        b1.write(data1)   

swapData()

