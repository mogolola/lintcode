"""
Question:

    Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers,
    which are ordered in lexicographical order. The index begins at 1.

Example:

    Given the permutation [1, 4, 2, 2], return 3

"""


#run out of memory

from itertools import permutations

class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        acc_index = 0
        while len(A) != 1:
            head = A[0]
            selected_digit = []
            for idx, digit in enumerate(A[1:]):
                sub_permit = A[1:]
                if digit < head:
                    if digit not in selected_digit:
                        sub_permit = sub_permit[:idx] + sub_permit[idx+1:]
                        sub_permit.append(head)
                        hash_map = {}
                        for j in sub_permit:
                            if j not in hash_map.keys():
                                hash_map[j] = 1
                            else:
                                hash_map[j] += 1
                        n = self.get_num_permutations(hash_map)
                        acc_index += n
                        selected_digit.append(digit)
            A.pop(0)
        return int(acc_index+1)

    def get_num_permutations(self, hash_map):
        n = sum(hash_map.values())
        num_permutations = self.factorial(n)
        for val in hash_map.values():
            num_permutations *= 1/(self.factorial(val))
        return num_permutations


    def factorial(self, n):
        r = 1
        for i in range(1, n+1):
            r = r * i

        return r





a = Solution()

print(a.permutationIndexII([10,10,10,10,9,8,7,6,5,4,3,2,1]))

"""

class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndexII(self, A):
        if A is None or len(A) == 0:
            return 0

        index = 1
        factor = 1
        for i in range(len(A) - 1, -1, -1):
            hash_map = {A[i]: 1}
            rank = 0
            for j in range(i + 1, len(A)):
                if A[j] in hash_map.keys():
                    hash_map[A[j]] += 1
                else:
                    hash_map[A[j]] = 1
                # get rank
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor / self.dupPerm(hash_map)
            factor *= (len(A) - i)

        return index


    def dupPerm(self, hash_map):
        if hash_map is None or len(hash_map) == 0:
            return 0
        dup = 1
        for val in hash_map.values():
            dup *= self.factorial(val)

        return dup


    def factorial(self, n):
        r = 1
        for i in range(1, n + 1):
            r *= i

        return r


a = Solution()

print(a.permutationIndexII([10,10,10,10,9,8,7,6,5,4,3,2,1]))

"""