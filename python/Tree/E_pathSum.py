# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if(root == None):
            return False
        
        sum -= root.val
        
        if(root.left == None and root.right == None):
            return sum == 0
        else:
            return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        
root = TreeNode(5)

rl = TreeNode(4)
rr = TreeNode(8)

root.left = rl
root.right = rr

rll = TreeNode(11)
rll.left = TreeNode(7)
rll.right = TreeNode(2)
rl.left = rll

rrl = TreeNode(13)
rrr = TreeNode(4)
rrr.right = TreeNode(1)
rr.left = rrl
rr.right = rrr

print(Solution().hasPathSum(root,22))
