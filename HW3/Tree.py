base=int(input())
n=1
space=int((base-1)/2)
print(space*" " + "*")
while (n+2)<=base:
    n+=2
    space-=1
    print(space*" " + n*"*")

