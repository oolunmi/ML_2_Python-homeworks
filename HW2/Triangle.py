a = float (input())
b = float (input())
c = float (input())

if a + b <= c:
   print ("No triangle") 
elif a + c <= b:
    print ("No triangle") 
elif c + b <= a:
    print ("No triangle")                
else:
    if c <= b:
        temp = c
        c = b
        b = temp
    if c < a:
        temp = c
        c = a
        a = c
    if c ** 2 == (a ** 2) + (b ** 2):
        print ("Right triangle")
    elif c ** 2 < (a ** 2) + (b ** 2):
        print ("Acute triangle")
    else:
        print ("Obtuse triangle") 
    
           

