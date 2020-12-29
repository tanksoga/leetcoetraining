# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
        
    def isSameTree(self, p, q):
        
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        #print(str(p.val) + "," + str(q.val))
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right,q.left) and self.isSameTree(p.left, q.right)
     
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.isSameTree(root,root)

root = TreeNode(1)   
rl = TreeNode(2)
rr = TreeNode(2)

root.left = rl
root.right = rr

rll = TreeNode(3)
rlr = TreeNode(4)

rl.left = rll
rl.right = rlr

rrl = TreeNode(4)
rrr = TreeNode(3)

rr.left = rrl
rr.right = rrr

print(Solution().isSymmetric(root))