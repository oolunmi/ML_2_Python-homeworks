numbers = list(map(float, input().split()))
print(numbers)
new_numbers=[]
for i in range(len(numbers)):
    new_item=sum(numbers[i:])
    new_numbers.append(new_item)
print(new_numbers)