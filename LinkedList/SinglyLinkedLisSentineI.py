# 链表操作---带哨兵
class LinkNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = LinkNode(666)

    # 寻找链表最后一个节点
    def find_last(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr

    # 在链表尾部添加
    def add_list(self,val):
        last = self.find_last()
        last.next = LinkNode(val)

    # 遍历链表
    def traverse_list(self):
        p = self.head.next
        while p:
            print(p.val)
            p = p.next

    # 给链表添加索引
    def find_node(self,index):
        i = -1
        p = self.head
        while p:
            if i == index:
                return p
            p = p.next
            i += 1

    # 根据索引得到值
    def get_value(self,index):
        node = self.find_node(index)
        # 当索引位置不正确时,抛出异常!
        if node == None:
            raise IndexError(index)
        return node.val

    # 在指定索引位置插入值
    def insert_value(self,index,val):
        prev = self.find_node(index - 1)
        if prev == None:
            raise IndexError(index)
        prev.next = LinkNode(val, prev.next)

    # 在指定索引删除值
    def remove_value(self,index):
        prev = self.find_node(index-1)      # 被删除节点的上一个节点
        if prev == None:
            raise IndexError(index)
        removed = self.find_node(index)     # 被删除的节点
        prev.next = removed.next

    # 在指定索引改变值
    def change_index_value(self,index,val):
        node = self.find_node(index)
        if node == None:
            raise IndexError(index)
        node.val = val



# 主函数
if __name__ == '__main__':
    list = LinkedList()
    list.add_list(1)
    list.add_list(2)
    list.insert_value(0,3)
    list.insert_value(0,4)
    list.remove_value(0)
    list.traverse_list()
    print(list.get_value(0))
