"""
Question:

    Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers,
    which are ordered in lexicographical order. The index begins at 1.

Example:

    Given the permutation [1, 4, 2, 2], return 3

"""



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

