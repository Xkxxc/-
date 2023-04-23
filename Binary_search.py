def binarySearch(list,target):
    left = 0
    right = len(left) - 1
    while left <= right:
        mid = (right+left) // 2
        if list[mid] == target:
            return mid
        elif target > list[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
