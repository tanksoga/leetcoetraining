# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        rev = []
        
        while head :
            rev.append(head.val)
            head = head.next
            
        return rev == rev[::-1]
        
l1 = ListNode(1)
l1_1 = ListNode(2)
l1_2 = ListNode(6)
l1_3 = ListNode(3)
l1_4 = ListNode(6)
l1_5 = ListNode(2)
l1_6 = ListNode(1)

l1.next = l1_1
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = l1_6

print(Solution().isPalindrome(l1))