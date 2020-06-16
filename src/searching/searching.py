def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


### Write an iterative implementation of Binary Search
def binary_search(arr, target):
    ## divide in half
    # if equals, return true
    # if smaller, return left half
    # else return right target
    # if at the end, return false
    # count = 0

    left_idx = 0
    right_idx = len(arr)-1
    # length = len(arr)
    while right_idx - left_idx >= 0:
        # count += 1
        # print(count)
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] > target:
            right_idx = mid_idx - 1
        elif arr[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            return mid_idx

    return -1  # not found
