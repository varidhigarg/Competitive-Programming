'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        q = [root]
        result=[]
        i=0
        while q :
            tmp = []
            result.append([])
            while q:
                x = q.pop(0)
                if x.left!=None:
                    tmp.append( x.left)
                if x.right is not None:
                    tmp.append(x.right)
                result[i].append(x.val)
            i+=1
            q=tmp
        
        return result[::-1]
                
            
            
        
'''
Linear Time
'''