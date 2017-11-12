'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        
        if m ==0:
            return
        n=len(matrix[0])
        rowBin = False
        colBin = False
        
        for x in range(m):
            if matrix[x][0]==0:
                rowBin=True
                break
        for x in range(n):
            if matrix[0][x]==0:
                colBin = True
                break
        
        for x in range(1,m):
            for y in range(1,n):
                if matrix[x][y]==0:
                    matrix[x][0]=0
                    matrix[0][y]=0
        
        for x in range(1,m):
            if matrix[x][0]==0:
                for y in range(1,n):
                    matrix[x][y]=0
        
        for y in range(1,n):
            if matrix[0][y]==0:
                for x in range(1,m):
                    matrix[x][y]=0
        if rowBin:
            for x in range(m):
                matrix[x][0]=0
                
        if colBin:
            for y in range(n):
                matrix[0][y]=0
                    
'''
Space - Constant
Time - Quadratic (Linear in terms of input)
'''