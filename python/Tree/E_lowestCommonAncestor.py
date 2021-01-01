# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return None
    
        pVal = p.val
        qVal = q.val
        
        current = root
        
        while current:
            currentVal = current.val
            print(str(currentVal) + "," + str(pVal) + "," + str(qVal))
            if pVal < currentVal and qVal < currentVal:
                current = current.left
            elif pVal > currentVal and qVal > currentVal :
                current = current.right
            else:
                return current
            
root = TreeNode(6)

rl = TreeNode(2)
rr = TreeNode(8)

root.left = rl
root.right = rr

rll = TreeNode(0)
rlr = TreeNode(4)
rl.left = rll
rl.right = rlr

rlrl = TreeNode(3)
rlrr = TreeNode(5)
rlr.left = rlrl
rlr.right = rlrr

rrl = TreeNode(7)
rrr = TreeNode(9)
rr.left = rrl
rr.right = rrr               
        
print(Solution().lowestCommonAncestor(root,TreeNode(2),TreeNode(8)).val)