#用二分查找寻找相同值的最左边
def binarysearchleftmost1(list,target):
    i = 0
    j = len(list) - 1
    candidate = -1
    while i <= j:
        m = (i + j) >> 1
        if target < list[m]:
            j = m -1
        elif list[m] < target:
            i = m + 1
        else:
            candidate = m
            j = m - 1
    return candidate

#返回更有用的值,例如[1,3,4,5,6],target = 2-->返回索引1,与上面对比,上面没有找到就返回-1.
def binarysearchleftmost2(list,target):
    i = 0
    j = len(list) - 1
    while i <= j:
        m = (i + j) >> 1
        if target <= list[m]:
            j = m - 1
        else:
            i = m + 1
    return i


