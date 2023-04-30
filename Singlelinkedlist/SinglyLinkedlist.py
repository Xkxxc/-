# 为链表节点类
class ListNode:
    def __init__(self, val=0, next=None):  # val为节点的值,next为指向下一节点的指针
        self.val = val
        self.next = next

# 为链表定义类
class LinkedList:
    def __init__(self):  # 初始化链表,设置头指针head为空
        self.head = None

    # 将节点添加到链表末尾的方法
    def add_node1(self, val):
        if not self.head:  # 首先判断链表是否为空,如果是空链表,则将新节点设置为头节点
            self.head = ListNode(val)
        else:  # 否则,遍历链表到尾节点,然后将尾节点的next指针指向新节点
            curr = self.head
            while curr.next:  # 如果curr.next不为空,则一直循环到链表最后
                curr = curr.next
            curr.next = ListNode(val)

    # 将节点添加到头部的方法
    def add_node2(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            curr = self.head
            self.head = ListNode(val)
            self.head.next = curr

    # 遍历链表
    def traverse_list(self):
        if not self.head:
            print("该链表为空")
        else:
            curr = self.head
            while curr:
                print(curr.val)
                curr = curr.next
            print("遍历完成")

    # 删除节点
    def delete_list(self,val):
        if not self.head:
            print("链表为空,无法删除!")
        # 删除头节点
        if val == self.head.val:
            next_node = self.head.next
            self.head = next_node
            print("删除成功")
        # 删除指定节点
        curr1 = self.head.next
        forerunner_node = self.head         # 设置前驱节点
        while curr1:
            if curr1.val == val:
                forerunner_node.next = curr1.next
                return 1
            forerunner_node = forerunner_node.next
            curr1 = curr1.next

    # 给链表添加索引
    def find_node(self,index):
        i = 0
        curr = self.head
        while curr:
            if index == i:
                return curr  # 返回地址
            curr = curr.next
            i += 1
        return None

    # 返回指定索引的值
    def get_value(self,index):
        node = self.find_node(index)
        if node == None:        #抛出异常
            raise Exception("在该索引没有找到该值")
        print(f"在索引{index}中的值是{node.val}")


    # 在指定位置插入值
    def insert_node(self,index,val):
        node = self.find_node(index-1)
        if node == None:  # 抛出异常
            raise Exception("索引值超过链表长度,插入失败")
        node.next = ListNode(val, node.next)

    # 在指定位置改变值
    def change_index_value(self,index,val):
        node = self.find_node(index)
        if node == None:
            raise IndexError(index)
        node.val = val

    # 链表遍历改值操作---把链表原先的值,改成其他值,例如1->2->3  将2改成4   缺点:如果有相同的值,就改较前一个---后续进行优化！
    def change_value(self,old_val,new_val)
        curr = self.head
        while curr:
            if curr.val == old_val:
                curr.val = new_val
                print("修改完成！")
                return 1
            curr = curr.next
        print("在链表中,没有找到改值,修改失败")

