'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

'''

from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = Counter(moves)
        if c['U']==c['D'] and c['L']==c['R']:
            return True
        return False
        '''
        print c
        out = False
        x,y=0,0
        for i in moves:
            if i=="U":
                y-=1
            elif i=="D":
                y+=1
            elif i=="L":
                x-=1
            else:
                x+=1
        if x==0 and y==0:
            return True
        return False
        '''
		
'''
Linear
'''