# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        answer = []
        if k == len(nums):
            return nums
        freq = {}
        # Count frequency
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Make heap queue
        freqList = [ (-1*a[1],a[0]) for a in freq.items() ]
        heapq.heapify(freqList)
        for i in range(k):
            answer.append(heapq.heappop(freqList)[1])
        
        return answer


ins = [3,0,1,0]
ink = 1
solution = Solution()
print(solution.topKFrequent(ins,ink))

