nums = [3,5,2,7,10,45,253,60,-1]

def merge(left, right):
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    return result+left if len(left) else result+right 



def divide(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    right = arr[mid:]
    left = arr[:mid]
    return merge(divide(right), divide(left))

print(divide(nums))