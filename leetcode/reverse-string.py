class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = ""
        for i in range(len(s)//2):
            print(s)
            tmp = s[i]
            s[i] = s[-1-i]
            s[-1-i] = tmp
        print(s)
solution = Solution()
solution.reverseString(["h","e","l","l","o"])
solution.reverseString(["H","a","n","n","a","h"])
