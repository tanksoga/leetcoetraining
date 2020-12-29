# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        
        passList = []
        
        while head:
            if head in passList:
                return passList.index(head)
            else:
                passList.append(head)
            head = head.next
            
        return None

l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(10)
l5 = ListNode(7)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l3

print(Solution().detectCycle(l1))