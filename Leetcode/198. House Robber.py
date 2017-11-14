'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        arr=[]
        
        for x in range(len(nums)):
            if x==0:
                arr.append(nums[x])
            else:
                if x-2>=0:
                    arr.append(max(nums[x]+arr[x-2],arr[x-1]))
                else:
                    arr.append(max(nums[x],arr[x-1]))
        return arr[-1]
'''
Linear Time
'''