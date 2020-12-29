# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        thisNode = result
        
        carry = result.val
        
        while l1 or l2:
            if(l1 and l2):
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif(not l2):
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l2.val + carry
                l2 = l2.next
                
                
            digit = sum % 10
            carry = sum / 10
            thisNode.val = digit

            if l1 or l2:
                thisNode.next = ListNode(carry)
                thisNode = thisNode.next
                
                
        if(carry != 0):
            thisNode.next = ListNode(carry)
            thisNode = thisNode.next
        '''
        while l1 and l2 :
            sum = l1.val + l2.val + carry
            
            digit = sum % 10
            carry = sum / 10
            
            print (str(sum) + "," + str(digit) + "," + str(carry))
            
            l1 = l1.next
            l2 = l2.next
            
            thisNode.val = digit
            
            if l1 or l2:
                thisNode.next = ListNode(carry)
                thisNode = thisNode.next
        '''
        
        return result

l1 = ListNode(2)
l1_1 = ListNode(4)
l1_2 = ListNode(3)

l1.next = l1_1
l1_1.next = l1_2

l2 = ListNode(5)
l2_1 = ListNode(6)
l2_2 = ListNode(4)

l2.next = l2_1
l2_1.next = l2_2
        
head = Solution().addTwoNumbers(l1,l2);

while head:
    print(int(head.val))
    head = head.next         
        