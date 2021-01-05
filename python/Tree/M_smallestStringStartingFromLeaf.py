# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        
        self.minResult = "zzzzzzzzzzzzzzzzzzzzzzzzzzzz"
        self.minDeep = 1000
        
        def dfsSearch(self, node, parentPath):
            """
            :type node: TreeNode
            :type parentPath: str
            """
            parentPath = str(chr(node.val + 97)) + parentPath

            if not node.left and not node.right:
                 if parentPath <= self.minResult:   
                    self.minDeep = len(parentPath)
                    self.minResult = parentPath
            else:
                if node.left:
                    dfsSearch(self, node.left, parentPath)
                if node.right:
                    dfsSearch(self, node.right, parentPath)
        
        if not root:
            return None
        
        if not root.left and not root.right:
            return chr(root.val + 97)
        
        dfsSearch(self, root,"")
        
        return self.minResult

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
rrr.left = TreeNode(5)
rrr.right = TreeNode(1)
rr.left = rrl
rr.right = rrr

print(Solution().smallestFromLeaf(root))