'''

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fact = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
        numbers=[x for x in range(1,n+1)]
        res=''
        k-=1
        while n>0:
            n=n-1
            i, k = divmod(k, fact[n])
            res += str(numbers[i])
            numbers.remove(numbers[i])
        return res
		
'''
Space - Linear
Time - Quadratic
'''