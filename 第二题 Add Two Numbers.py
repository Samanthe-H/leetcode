# 2. 两数相加
# 初始提交：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 将节点类定义成Node，该类在初始化实例对象时，定义了两个实例变量，其中data用来存储节点的值，next用来存储下一个节点的索引
class Solution:
    def addTwoNumbers(self, l1, l2) :
        '''
        type l1: ListNode
        type l2: ListNode
        rtype: ListNode
        '''
        v1 = l1.val + l2.val
        l3 = ListNode(v1%10)
        l3.next = ListNode(v1//10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while True: # while循环为了运行else之后的内容
            if p1 and p2:
                v = p1.val + p2.val + p3.next.val
                p3.next.val = v % 10
                p3.next.next = ListNode(v//10)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                v = p1.val + p3.next.val
                p3.next.val = v % 10
                p3.next.next = ListNode(v//10)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                v = p2.val + p3.next.val
                p3.next.val = v % 10
                p3.next.next = ListNode(v//10)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3

# 优化1：
