# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        
        def findAllPath(self, node, parentPath): 
            if parentPath != "" :
                currentPath = parentPath + str(node.val)
            else:
                currentPath = str(node.val)
            
            if not node.left and not node.right:
                #pathResult.append(currentPath)
                self.total += int(currentPath)
            else:
                if node.left:
                    findAllPath(self, node.left, currentPath)
                if node.right:
                    findAllPath(self, node.right, currentPath)
                    
        if not root:
            return 0
        
        if not root.left and not root.right:
            return root.val            
        
        findAllPath(self, root, "")
        
        return self.total

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

print(Solution().sumNumbers(root))