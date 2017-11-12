'''
Write a function to find the longest common prefix string amongst an array of strings.

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n==0:
            return ""
        elif n==1:
            return strs[0]
        
        res=""
        flag=False
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for j in range(1,n):
                if len(strs[j])>i:
                    if strs[j][i]!=tmp:
                        flag=True
                        break
                else:
                    flag=True
                    break
            if flag:
                break
            res+=tmp
        return res
            
'''
Space - Constant
Time - Linear in terms of input
'''