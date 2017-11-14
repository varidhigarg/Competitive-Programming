'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        queue = [root]
        while queue:
            tmp_queue = []
            
            while queue:
                ele = queue.pop(0)
                if ele!=None:
                    tmp_queue.append(ele.left)
                    tmp_queue.append(ele.right)
            length = len(tmp_queue)
            for x in range(length/2):
                a = tmp_queue[x]
                b = tmp_queue[length-x-1]
                
                if a!=b:
                    if a is None or b is None:
                        return False
                    elif a.val!=b.val:
                            return False
                
                    
            queue=tmp_queue
        return True
            
			
'''
Time - Linear
'''