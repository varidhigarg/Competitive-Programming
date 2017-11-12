'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        arr=[[1]*n for _ in xrange(m)]
        
        for x in xrange(1,m):
            for y in xrange(1,n):
                arr[x][y] = arr[x-1][y]+arr[x][y-1]
               
        return arr[m-1][n-1]

'''
Space, Time - Quadratic
DP Solution
'''