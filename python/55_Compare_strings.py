"""
Question:
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example:
For A = "ABCD", B = "ACD", return true.

For A = "ABCD", B = "AABC", return false.

"""


class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here
        contain = True

        hash_map_A = {}
        hash_map_B = {}

        for c in A:
            if c in hash_map_A.keys():
                hash_map_A[c] += 1
            else:
                hash_map_A[c] = 1

        for c in B:
            if c in hash_map_B.keys():
                hash_map_B[c] += 1
            else:
                hash_map_B[c] = 1

        for c in hash_map_B.keys():
            if c not in hash_map_A.keys():
                contain = False
                break
            elif hash_map_A[c] < hash_map_B[c]:
                contain = False
                break

        return contain