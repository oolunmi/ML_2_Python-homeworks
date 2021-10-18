n = int(input())
Product = 1

while n != 0:
    if n % 10 != 0:
     Product *= n % 10
    n //= 10
print ("Digit product:", Product)