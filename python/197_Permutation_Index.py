"""
Question:
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which
are ordered in lexicographical order. The index begins at 1.

Example:
Given [1,2,4], return 1.

"""


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndex(self, A):
        # write your code here
        index = 1
        for idx, digit in enumerate(A):
            pointer = A[idx]
            candidates = A[idx + 1:]
            if candidates != []:
                for c in candidates:
                    if c < pointer:
                        n = len(candidates)
                        index += self.factorial(n)
        return index

    def factorial(self, n):
        print(n)
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r