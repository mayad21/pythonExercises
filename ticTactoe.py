class Solution(object):
    def validTicTacToe(self, board):
        #return false if there's more o's than x's 
        #return false if there's 2 more x's than o's
        countX = 0
        countO = 0
        for i in range(3):
            for j in board[i]:
                if j == 'X':
                    countX+= 1
                elif j == "O":
                    countO+=1
        if countO > countX or countX - countO > 1:
            return False

        #return false if too wins
        #check for rows wins
        winX = 0
        winO = 0
        for i in range(3):
            if board[i] == "XXX":
                winX += 1
            elif board[i] == "OOO":
                winO += 1
                #[0][0] [1][1] [2][2]   [1][3][2,2][3][1]
        for i in range(3):
            if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
                winX += 1
            if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
                winO += 1
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                winX += 1
        if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
                winO += 1
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                winO += 1
        if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
                winX += 1
        if winO > 1:
            return False
        if winX > 2:
            return False
        if winX and winO:
            return False
        if winX and countX <= countO:
            return False
        if winO and countX > countO:
            return False
        return True
              



        """
        :type board: List[str]
        :rtype: bool
        """