# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        if head.next == None:
            return head
        
        prev = None
        current = head
        
        while current:
            oriNext = current.next
            current.next = prev
            prev = current
            current = oriNext
            
        return prev
            
l1 = ListNode(1)
l1_1 = ListNode(2)
l1_2 = ListNode(6)
l1_3 = ListNode(3)
l1_4 = ListNode(4)
l1_5 = ListNode(5)
l1_6 = ListNode(6)

l1.next = l1_1
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = l1_6

l = Solution().reverseList(l1)

while l:
    print(l.val)
    l = l.next                
        