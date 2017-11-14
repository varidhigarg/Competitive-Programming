'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        output=""
        while n > 0:
            r = (n-1)%26
            n= (n-1)//26
            output=chr(65+r)+output
            
        return output
            
'''
Linear 
'''