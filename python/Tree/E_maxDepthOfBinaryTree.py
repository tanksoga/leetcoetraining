# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None :
            return 0
        else:
            leftH = self.maxDepth(root.left)
            rightH = self.maxDepth(root.right)
            return max(leftH,rightH) + 1
        
root = TreeNode(3)   
rl = TreeNode(9)
rr = TreeNode(20)

root.left = rl
root.right = rr

rrl = TreeNode(15)
rrr = TreeNode(7)

rr.left = rrl
rr.right = rrr

print(Solution().maxDepth(root))