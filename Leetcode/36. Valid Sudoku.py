'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for x in range(9):
            tmp = [0]*10
            tmp2 = [0]*10
            for y in range(9):
                
                if board[x][y]!='.':
                    ind = int(board[x][y])
                    if tmp[ind]!=0:
                        return False
                    tmp[ind] = 1
                if board[y][x]!='.':
                    ind = int(board[y][x])
                    if tmp2[ind]!=0:
                        return False
                    tmp2[ind] = 1
                    
        for x in range(0,9,3):
            for y in range(0,9,3):
                tmp = [0]*10
                for a in range(3):
                    for b in range(3):
                        if board[x+a][y+b]!='.':
                            ind = int(board[x+a][y+b])
                            if tmp[ind]!=0:
                                return False
                            tmp[ind]=1
                
        
        
        return True
		
		
'''
Quadratic Time
'''