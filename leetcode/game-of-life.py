# https://leetcode.com/problems/game-of-life/
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        def isIn(a,b):
            return True if a<m and a>=0 and b<n and b>=0 else False
        originB = [ [ board[a][b] for b in range(n) ] for a in range(m) ]
        for i in range(m):
            for j in range(n):
                alive = 0
                if isIn(i-1,j-1) and originB[i-1][j-1]:
                    alive += 1
                if isIn(i-1,j) and originB[i-1][j]:
                    alive += 1
                if isIn(i-1,j+1) and originB[i-1][j+1]:
                    alive += 1
                if isIn(i,j+1) and originB[i][j+1]:
                    alive += 1
                if isIn(i+1,j+1) and originB[i+1][j+1]:
                    alive += 1
                if isIn(i+1,j) and originB[i+1][j]:
                    alive += 1
                if isIn(i+1,j-1) and originB[i+1][j-1]:
                    alive += 1
                if isIn(i,j-1) and originB[i][j-1]:
                    alive += 1
                print(i,j,alive)
                if originB[i][j]:
                    if alive==2 or alive==3:
                        print("ALIVE")
                        board[i][j] = 1
                    else:
                        print("DEAD")
                        board[i][j] = 0
                else:
                    if alive==3:
                        print("RE-LIVE")
                        board[i][j] = 1
        return



# ina = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
ina = [[1,1],[1,0]]
solution = Solution()
for i in ina:
    print(i)
print('-----------------')
solution.gameOfLife(ina)
for i in ina:
    print(i)
