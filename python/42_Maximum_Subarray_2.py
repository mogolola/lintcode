"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.

"""





"""
# Very greedy, run out of time budget
class Solution:
    
    def maxTwoSubArrays(self, nums):
        # write your code here
        max_sum = -10000
        for idx, num in enumerate(nums):
            max_left = self.get_max_sum(nums[:idx+1])
            max_right = self.get_max_sum(nums[idx+1:])
            max_sum = max(max_sum, max_left + max_right)
        return max_sum
    
    
    def get_max_sum(self, nums):
        sum = 0
        max_sum = -10000
        min_sum = 0
        for idx, num in enumerate(nums):
            min_sum = min(sum, min_sum)
            sum += num
            max_sum = max(max_sum, sum - min_sum)

        return  max_sum
"""


#Use dynamic programming, avoid duplicated computation

class Solution:

    def maxTwoSubArrays(self, nums):
        Max_array_forward = self.forward(nums)
        Max_array_backward = self.backward(nums)
        Max_array_backward = Max_array_backward[::-1]
        max_sum = -1000
        for i in range(len(nums)-1):
            max_sum = max(Max_array_forward[i] + Max_array_backward[i+1], max_sum)
        return max_sum



    def forward(self, nums):
        max_values = []
        _sum = 0
        _max = -10000
        for n in nums:
            _sum += n
            _max = max(_max, _sum)
            _sum = max(_sum,0)
            max_values.append(_max)
        return  max_values

    def backward(self, nums):
        max_values = []
        _sum = 0
        _max = -10000
        for n in nums[::-1]:
            _sum += n
            _max = max(_max, _sum)
            _sum = max(_sum, 0)
            max_values.append(_max)
        return  max_values


a = Solution()
print(a.maxTwoSubArrays([1, 3, -1, 2, -1, 2]))

