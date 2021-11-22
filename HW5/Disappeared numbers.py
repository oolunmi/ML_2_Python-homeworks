nums = [4,3,2,7,2,2,3,1]

def disappeared_numbers(nums):
    n=len(nums)
    missing=[]
    for i in range(1,n+1):
        if i not in nums:
            missing.append(i)
    return missing

print(disappeared_numbers(nums))




