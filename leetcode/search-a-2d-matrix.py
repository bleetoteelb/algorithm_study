# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        rStart, rEnd, cStart, cEnd = 0, len(matrix)-1, 0, len(matrix[0])-1
        targetRow = (rStart + rEnd+1)//2
        while(True):
            if matrix[targetRow][0] > target:
                rEnd = targetRow - 1
            elif matrix[targetRow][0] <= target and matrix[targetRow][-1] >= target:
                break
            elif targetRow+1 < len(matrix) and matrix[targetRow+1][0] <= target:
                rStart = targetRow +1
            else:
                return "false"
            targetRow = (rStart + rEnd+1)//2

        targetCol = (cStart + cEnd+1)//2
        while(True):
            if matrix[targetRow][targetCol] == target:
                return "true"
            elif matrix[targetRow][targetCol] > target:
                cEnd = targetCol-1
            else:
                cStart = targetCol+1
            targetCol = (cStart + cEnd+1)//2
            if cStart >= cEnd:
                break
        if matrix[targetRow][targetCol] == target:
            return "true"
        else:
            return "false"



inputMatrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
solution = Solution()
print(solution.searchMatrix(inputMatrix, 13)) # false
print(solution.searchMatrix(inputMatrix, 4))  # false
print(solution.searchMatrix(inputMatrix, 50)) # false
print(solution.searchMatrix(inputMatrix, 80)) # false
print(solution.searchMatrix(inputMatrix, 3)) # true
print(solution.searchMatrix(inputMatrix, 20)) # true
print(solution.searchMatrix(inputMatrix, 23)) # true
        
