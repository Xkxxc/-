#问题引出,如果要查找的值始终在左边,假设循环次数是L次,那么需要进行L次判断,如果始终在最右边,那么就需要2*L次
#所以为了使无论查找的值是在左边还是右边,都进行L次判断。就有了该平衡版二分查找
def binarysearch3(list,target):
    i = 0
    j = len(list)
    while 1 < j-i:    #此循环条件意思是,列表范围里还有多少元素,如果列表范围内仅剩余一个元素,则跳出循环
        m = (i + j) >> 1
        if target < list[m]:
            j = m
        else:
            i = m
    if list[i] == m:
        return m
    else:
        return -1

