'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==0:
            return 0
        if n<4:
            return max(nums)
        
        arr=[nums[0],max(nums[1],nums[0])]
        
        for x in range(2,n-1):
            arr.append(max(nums[x]+arr[x-2],arr[x-1]))
                
        m1=arr[-1]
        arr=[0,nums[1]]
        for x in range(2,n):
            arr.append(max(nums[x]+arr[x-2],arr[x-1]))
        return max(m1,arr[-1])     
        
                    
'''
DP Solution
Linear Time and Space
'''