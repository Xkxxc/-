def binarysearch(list,target):
    i = 0
    j = len(list)
    while i < j:    #不要写<=,如果要查找的值不在列表中,则会造成死循环!
        m = (i + j) >> 1
        if target < list[m]:
            j = m
        elif list[m] < target:
            i = m - 1
        else:
            return m
    return -1

