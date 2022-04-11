# https://leetcode.com/problems/shift-2d-grid/
from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        answer = []
        joinGrid = []
        for g in grid:
            joinGrid += g
        shiftNum = k % len(joinGrid)
        joinSize = len(joinGrid)
        pos = joinSize-shiftNum
        m = len(grid)
        n = len(grid[0])
        print(shiftNum,m,n,joinGrid)
        for i in range(m):
            if pos + n < joinSize:
                answer.append(joinGrid[pos:pos+n])
                pos += n
            else:
                answer.append(joinGrid[pos:]+joinGrid[:n-joinSize+pos])
                pos = n-joinSize+pos
            print(answer)

        return answer


ing = [[1]]
ink = 100
solution = Solution()
print(solution.shiftGrid(ing,ink))
