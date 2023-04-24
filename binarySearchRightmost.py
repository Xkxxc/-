#用二分查找寻找相同值的最右边
def binarysearchleftmost(list,target):
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
            i = m + 1
    return candidate

