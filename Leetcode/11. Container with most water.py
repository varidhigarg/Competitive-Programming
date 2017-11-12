'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater,i,j=0,0,len(height)-1
        while i<j:
            tmp = height[j] if height[j]<height[i] else height[i]
            tmp *= (j-i)
            maxWater = maxWater if maxWater>tmp else tmp
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxWater
		
'''
Space - Constant
Time - Linear
'''