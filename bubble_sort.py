nums = [3,5,2,7,10,45,253,60,-1]

for i in range(len(nums)-1):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = tmp

print(nums)