# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = [(root,1)]
        
        count = 0
        
        while count < len(nodes):
            node, index = nodes[count]
            count += 1
            if node:
                nodes.append((node.left,index * 2))
                nodes.append((node.right, index * 2 + 1))
                
        return nodes[-1][1] == len(nodes)
        