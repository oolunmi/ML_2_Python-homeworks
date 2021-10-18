def n_of_divisors(n):
    lim = n//2
    count_div = 0
    for i in range(1,lim+1):
        if n % i == 0:
            count_div+=1
    print(count_div+1)
n_of_divisors(3)
