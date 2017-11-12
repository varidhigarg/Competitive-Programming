'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for x in range(n)]
        i=0
        j=0
        a=0
        b=1
        for k in xrange(1,n*n+1):
            res[i][j] = k
            if res[(i+a)%n][(j+b)%n]!= 0:
                a, b = b, -a
            i += a
            j += b
        return res
        
'''
Time - Quadratic
Space - Quadratic for output
'''
