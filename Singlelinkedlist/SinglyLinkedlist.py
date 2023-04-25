# 为链表节点类
class ListNode:
    def __init__(self, val=0, next=None):   # val为节点的值,next为指向下一节点的指针
        self.val = val
        self.next = next

# 为链表定义类
class LinkedList:
    def __init__(self):         # 初始化链表,设置头指针head为空
        self.head = None

    # 将节点添加到链表末尾的方法
    def addNode(self, val):
        if not self.head:       # 首先判断链表是否为空,如果是空链表,则将新节点设置为头节点
            self.head = ListNode(val)
        else:       # 否则,遍历链表到尾节点,然后将尾节点的next指针指向新节点
            curr = self.head
            while curr.next:        # 如果curr.next不为空,则一直循环
                curr = curr.next
            curr.next = ListNode(val)
