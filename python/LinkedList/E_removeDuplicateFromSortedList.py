# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return head
        
        nextNode = head.next
        thisNode = head
        
        while nextNode:
            if(nextNode.val == thisNode.val):
                thisNode.next = nextNode.next
                nextNode = nextNode.next
            else:
                thisNode = thisNode.next
                nextNode = nextNode.next
            
        return head
        
l1 = ListNode(1)
l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(6)
l1_4 = ListNode(6)

l1.next = l1_1
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = None

l = Solution().deleteDuplicates(l1)
while l:
    print(l.val)
    l = l.next