# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        rStart, rEnd, cStart, cEnd = 0, len(matrix)-1, 0, len(matrix[0])-1
        print(rStart, rEnd, cStart, cEnd)
        targetRow = (rStart + rEnd)//2
        print(targetRow)
        print("------------")
        while(True):
            print(rStart,rEnd,targetRow)
            if matrix[targetRow][0] < target:
                rEnd = targetRow
            else:
                rStart = targetRow
            targetRow = (rStart + rEnd)//2
            if rStart == rEnd:
                break

        print("------------")
        print("targetRow",targetRow)
        targetCol = (cStart + cEnd)//2
        print(targetCol)
        print("------------")
        while(True):
            print(cStart,cEnd,targetCol)
            if matrix[targetRow][targetCol] < target:
                cEnd = targetCol
            else:
                cStart = targetCol
            targetCol = (cStart + cEnd)//2
            if cStart == cEnd:
                break
        print("targetCol",targetCol)
        if matrix[targetRow][targetCol] == target:
            return "true"
        else:
            return "false"



inputMatrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
inputTarget = 11
solution = Solution()
print(solution.searchMatrix(inputMatrix, inputTarget))
        
