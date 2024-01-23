def generate(nums):
    i, j = 0, 1
    count = 0
    while j<len(nums):
        if nums[j]> nums[j-1]:
            j+=1
        else:
            n = j - i
            count+= n*(n+1)//2
            i = j
            j+=1
    n = j - i
    count+= n*(n+1)//2
    return count
nums = [7, 8 , 9, 1, 2, 3, 4]
print(generate(nums))