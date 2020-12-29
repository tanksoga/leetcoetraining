# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):

    #def main():
    #    l1 = [1,2,4]
    #    l2 = [1,3,4]

    #    print(mergeTwoLists(l1,l2))
    
    def mergeTwoLists(self,l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

l1 = ListNode(1)
l1_1 = ListNode(2)
l1_2 = ListNode(4)

l1.next = l1_1
l1_1.next = l1_2
l1_2.next = None

l2 = ListNode(1)
l2_1 = ListNode(3)
l2_2 = ListNode(4)

l2.next = l2_1
l2_1.next = l2_2
l2_2.next = None

head = Solution().mergeTwoLists(l1,l2)

while head:
    print(head.val)
    head = head.next        