# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        def dfsSearch(self, node, parentPath , remain):
            """
            :type node: TreeNode
            :type parentPath: List
            :type remain: int
            """
            
            remain = remain - node.val
            
            parentPath.append(node.val)

            if not node.left and not node.right and (remain == 0):
                currentPath = list(parentPath)
                result.append(currentPath)
            else:
                if node.left:
                    currentPath = list(parentPath)
                    dfsSearch(self, node.left, currentPath, remain)
                if node.right:
                    currentPath = list(parentPath)
                    dfsSearch(self, node.right, currentPath, remain)
        
        if not root:
            return None
        
        if not root.left and not root.right:
            if sum - root.val == 0:
                return [[root.val]]
            else:
                return []
        
        result = []
        
        dfsSearch(self, root,[],sum)
                
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
rrr.left = TreeNode(5)
rrr.right = TreeNode(1)
rr.left = rrl
rr.right = rrr

print(Solution().pathSum(root,22))