'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for x in nums:
            if total<2 or nums[total-2]!=x:
                nums[total]=x
                total+=1
              
        return total
                
				
'''
Space - Constant
Time - Linear
'''