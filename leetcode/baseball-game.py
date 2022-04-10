# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops) -> int:
        st = []
        pos = 0
        for i in ops:
            if i == "+":
                st.append(st[-1] + st[-2])
            elif i == "D":
                st.append(st[-1]*2)
            elif i == "C":
                del st[-1]
            else:
                st.append(int(i))
        return sum(st)


ins = ["5","-2","4","C","D","9","+","+"]
solution = Solution()
print(solution.calPoints(ins))

