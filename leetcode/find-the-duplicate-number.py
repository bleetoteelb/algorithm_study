class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        tmp_nums = [0] * (size)
        for i in range(size):
            if tmp_nums[nums[i]-1] == 0:
                tmp_nums[nums[i]-1] = 1
            else:
                return nums[i]
