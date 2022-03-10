def driver(speed):
    if speed<=70:
        print(speed)
    elif speed>70:
        i=0
        s=70
        while s<speed:
            i+=1
            s+=5
        if i<12:
            print(i)
        else:
            print("liscence suspend")
speed=int(input("enter:"))
driver(speed)



