'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getLength(self,root):
        if root is None:
                return 0
        left  = self.getLength(root.left)
        if left==-1:
            return -1
        right = self.getLength(root.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getLength(root)!=-1
        
'''
Linear Time
'''