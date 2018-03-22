'''

Question:
Count the number of k's between 0 and n. k can be 0 - 9.

Example:
if n = 12, k = 1 in
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
we have FIVE 1's (1, 10, 11, 12)


'''




class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        k = str(k)
        count = 0
        for i in range(0,n+1):
            digit = str(i)
            if k in digit:
                count += digit.count(k)
        return count