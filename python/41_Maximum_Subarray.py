"""
Question:
Given an array of integers, find a contiguous subarray which has the largest sum.

Example:
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

time complexity should be O(n)

"""

"""
# Greedy, run out of time budget

class Solution:
    
    def maxSubArray(self, nums):
        # write your code here
        t = len(nums)
        maxi = nums[0]
        left = 0
        right = 1
        for idx, n in enumerate(nums):
            if n < 0:
                continue
            i = idx
            j = idx +1
            while j < t:
                if nums[j] >= 0:
                    _sum = sum(nums[i:j+1])
                    if _sum < 0:
                        break
                    if _sum >=maxi:
                        left = i
                        right = j+1
                        maxi = _sum
                j += 1
        return maxi
"""

"""

# A smarter Greedy, time complexity O(n)

class Solution:

    def maxSubArray(self, nums):
        sum = 0
        max_value = -10000 # minimum interger
        for num in nums:
            sum = max(sum, 0)
            sum += num
            max_value = max(max_value, sum)
        return max_value

"""

# Dynamic programming

class Solution:

    def maxSubArray(self, nums):
        sum = 0
        max_sum = -10000
        min_sum = 0
        for idx, num in enumerate(nums):
            min_sum = min(sum, min_sum)
            sum += num
            max_sum = max(max_sum, sum - min_sum)

        return  max_sum




a = Solution()
print(a.maxSubArray([-1,0,1]))