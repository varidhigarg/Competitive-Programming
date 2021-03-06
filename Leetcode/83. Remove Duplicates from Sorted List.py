'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return
        tmp=head
        while tmp.next!=None:
            if tmp.val==tmp.next.val:
                if tmp.next.next!=None:
                    tmp.next=tmp.next.next
                else:
                    tmp.next=None
            else:
                tmp=tmp.next
        
        return head
		
'''
Time - Linear
Space - Constant
'''