'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        arr=[[0]*n for _ in xrange(m)]
        arr[0][0]=1
        for x in xrange(1,m):
            if obstacleGrid[x-1][0]== 0:
                arr[x][0]=arr[x-1][0]
            else:
                break
        for x in xrange(1,n):
            if obstacleGrid[0][x-1]== 0:
                arr[0][x]=arr[0][x-1]
            else:
                break
        for x in xrange(1,m):
            for y in xrange(1,n):
                a = arr[x][y-1] if obstacleGrid[x][y-1]==0 else 0
                b = arr[x-1][y] if obstacleGrid[x-1][y]==0 else 0
                arr[x][y]=a+b
                
        return arr[m-1][n-1]
                
'''
Space, Time - Quadratic with additional constant factor from part one
DP Solution
'''