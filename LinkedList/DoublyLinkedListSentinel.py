# 双向链表操作——带哨兵
class LinkNode:
    def __init__(self,val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = LinkNode(666)       # 设置头节点
        self.tail = LinkNode(777)       # 设置尾节点
        self.head.next = self.tail
        self.tail.prev = self.head

    # 根据索引查找节点
    def findnode(self,index):
        i = -1      # 因为有头哨兵所以设置为-1,不再是0
        p = self.head
        while p != self.tail:       # 尾哨兵不存储数据,故循环到尾哨兵即可
            if i == index:
                return p
            p = p.next
            i += 1
        return None

    # 根据索引位置插入值
    def insert(self,index,val):
        prev = self.findnode(index-1)
        if prev == None:    # 输入的index不合法
            raise IndexError(index)
        next = prev.next
        inserted = LinkNode(val,prev,next)
        prev.next = inserted
        next.prev = inserted

    # 根据索引删除元素
    def remove(self,index):
        prev = self.findnode(index-1)
        if prev == None:
            raise IndexError(index)
        removed = prev.next
        if removed == self.tail:
            raise IndexError(index)
        next = removed.next
        prev.next = next
        next.prev = prev

    # 双向链表的特点——利用尾哨兵——在链表尾部添加值
    def addLast(self,val):
        last = self.tail.prev   # 尾节点
        last.next = LinkNode(val,last,self.tail)    # 将原来的尾节点指向添加的节点
        self.tail.prev = last.next      # 将尾哨兵的上一个节点指向为节点,实现双向

    # 双向链表的特点——利用尾哨兵——在链表尾部删除值
    def removeLast(self):
        last = self.tail.prev   # 尾节点
        # 如果尾哨兵的上一个节点为头哨兵,则抛出异常
        if last == self.head:
            raise IndexError(0)
        last.prev.next = self.tail      # 将尾节点的上一个节点的下一个节点指向尾哨兵
        self.tail.prev = last.prev      # 将尾哨兵指向尾节点的上一个节点



    # 遍历链表
    def traverse_list(self):
        p = self.head.next
        while p != self.tail:
            print(p.val)
            p = p.next


if __name__ == '__main__':
    list = LinkedList()
    list.insert(0,3)
    list.insert(0,2)
    list.insert(0,1)
    list.addLast(4)
    list.removeLast()
    list.traverse_list()

