'''
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or k==0 or head.next==None:
            return head
        
        end,n = head,0
        
        while end!=None:
            end=end.next
            n+=1
        
            
        k=n-k%n-1
        
        tmp = head
        while k>0:
            k-=1
            tmp=tmp.next
        end = tmp.next
        if end==None:
            return head
        tmp.next=None
        tmp = end
        while tmp.next!=None:
            tmp = tmp.next
        tmp.next = head
        return end
		
'''
Space - Constant
Time - Linear
'''