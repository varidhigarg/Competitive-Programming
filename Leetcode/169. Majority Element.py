'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr=nums[0]
        count=1
        for x in nums[1:]:
            if x==curr:
                count+=1
            else:
                if count==1:
                    curr=x
                else:
                    count-=1
        return curr
		
'''
Linear Time
'''