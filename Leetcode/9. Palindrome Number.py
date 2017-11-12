'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        divisor = 1;
        while (x / divisor >= 10):
            divisor *= 10

        while (x != 0):
            leading = x/ divisor; 
            trailing = x % 10;

            if (leading != trailing): 
                return False

            x = (x % divisor) / 10;

            divisor = divisor / 100;
        
        return True
		
'''
Space - Constant
Time - log(n)
'''