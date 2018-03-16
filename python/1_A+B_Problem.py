"""
Question:
Write a function that add two numbers A and B. You should not use + or any arithmetic operators.

Example:
Given a=1 and b=2 return 3

"""
MAX_BIT = 2 ** 32
MAX_BIT_COMPLIMENT = -2 ** 32


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """

    def aplusb(self, a, b):
        # write your code here
        carry = 1
        while carry != 0:
            s = a ^ b
            carry = (a & b) << 1
            a = s
            b = carry
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
        return s


