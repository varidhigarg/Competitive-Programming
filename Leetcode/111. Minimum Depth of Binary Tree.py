'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        q = [root]
        n=1
        while q:
            tmp_q=[]
            while q:
                ele = q.pop(0)
                if ele.left==None and ele.right==None:
                    return n
                else:
                    if ele.left:
                        tmp_q.append(ele.left)
                    if ele.right:
                        tmp_q.append(ele.right)
            q=tmp_q
            n+=1
        return n
        
                
'''
Linear Time
BFS
'''