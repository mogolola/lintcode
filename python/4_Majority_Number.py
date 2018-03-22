

'''
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

Example
Given [1, 1, 1, 1, 2, 2, 2], return 1

'''




class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        candidates = set(nums)
        size = len(nums)
        for i in candidates:
            if nums.count(i) >= 0.5 * size:
                return i