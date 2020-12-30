# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def printTree(self, root):
    
        if root == None:
            return None
        else:
            print(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root is None :
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
        

        

            
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

Solution().printTree(Solution().invertTree(root))