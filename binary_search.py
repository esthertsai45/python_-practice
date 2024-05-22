nums = [-1, 2, 3, 5, 7, 10, 45, 60, 253]


def search(nums, target):    
    left = 0
    right = len(nums)-1
    
    while(left <= right):
        mid = (left+right) //2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
    
print(search(nums, 5))
print(search(nums, -1))
print(search(nums, 0))