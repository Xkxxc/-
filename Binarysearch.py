def binarySearch(list,target):
    """
    该函数用于实现二分查找
    :param list: 传入一个有序且升序的列表（允许相邻的两个值相等）
    :param target: 传入想要查找的值
    :return: 返回想要查找的值的索引,如果没找到,则返回-1
    """
    i = 0   #设置左索引
    j = len(list) - 1   #设置右索引
    while i <= j:   #左索引不能大于右索引
        #如果索引过大,相加起来超过了int可以表示的范围,就有可能出现负数,这是因为我们所输入的十进制都会转化成二级制供计算机识别,计算机的首位通常作为符号位
        m = (i + j) // 2    #设置中间索引——————建议使用m = (i + j) >> 1
        if target > list[m]:    #如果在右边,则重新赋值左索引为中间索引+1
            i = m+1 
        elif target < list[m]:    #如果在左边,则重新赋值右索引为中间索引-1
            j = m-1
        else:    #恰好想要查找的值等于list[m],则返回索引值m
            return m
    return -1   #没有找到返回-1
