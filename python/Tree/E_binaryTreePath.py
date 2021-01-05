# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfsSearch(self, node, parentPath):
            
            if parentPath != "" :
                currentPath = str(parentPath) + "->" + str(node.val)
            else:
                currentPath = str(node.val)
            
            if not node.left and not node.right:
                result.append(currentPath)
            else:
                if node.left:
                    dfsSearch(self, node.left, currentPath)
                if node.right:
                    dfsSearch(self, node.right, currentPath)
        
        if not root:
            return None
        
        if not root.left and not root.right:
            return [str(root.val)]
        
        result = []
        
        dfsSearch(self, root,"")
                
        return result
        
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

print(Solution().binaryTreePaths(root))