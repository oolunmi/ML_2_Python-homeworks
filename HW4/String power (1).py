original=str(input())
power=int(input())
if power>0:
    string=original*power
    print(string)
if power==0:
    print("")
else:
    if len(original)%int(-1*power)!=0:
        print(str(power)+" power of this string is undefined.")
    else:
        new_len=int(len(original)//(-1*power))
        part=original[0:new_len]
        can_be_defined=True
        for i in range(0,len(original),new_len):
            part_i=original[i:(i+new_len)]
            if part_i!=part:
                print(str(power)+" power of this string is undefined.")
                can_be_defined=False
                break
        if can_be_defined is True:
            print(part)






      


