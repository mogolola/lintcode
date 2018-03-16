"""
Question:
Write an algorithm which computes the number of trailing zeros in n factorial.

Example:
11! = 39916800, so the out should be 2

"""


"""
#Run out of time budget
class Solution:
    
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        hash_map = {'5':0, '0':0}
        for i in range (1,n+1):
            str_digit = str(i)
            if str_digit[-1] in hash_map.keys():
                print('----------', str_digit)
                while str_digit[-1] in hash_map.keys():
                    if str_digit[-1] == '0':
                        hash_map['0'] += 1
                        print(str_digit[-1])
                        str_digit = str_digit[:-1]
                        if len(str_digit) == 0:
                            break
                    else:
                        hash_map['5'] += 1
                        print(5)
                        j = 2
                        while (int(str_digit) % (5^j)) == 0:
                            hash_map['5'] += 1
                            print(5)
                            j += 1
                        break


        print(hash_map)
        return hash_map['0'] + hash_map['5']
"""

# simply realize log_5(n)

class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        if n < 0:
            return -1

        count = 0
        while n > 0:
            n = int(n/5)
            count += n

        return count



a = Solution()
print(a.trailingZeros(105))