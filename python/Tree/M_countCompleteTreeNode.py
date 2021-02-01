#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

root = TreeNode(3)   
rl = TreeNode(9)
rr = TreeNode(20)

root.left = rl
root.right = rr

rrl = TreeNode(15)
rrr = TreeNode(7)

rr.left = rrl
rr.right = rrr

print(Solution().countNodes(root))