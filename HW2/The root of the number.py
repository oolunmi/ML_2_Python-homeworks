def root(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    print(sum_digits)
    while sum_digits >= 10:
        sum_digits = root(sum_digits)
    return sum_digits

