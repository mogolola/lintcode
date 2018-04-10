
'''
The words are same rotate words if rotate the word to the right by loop, and get another. Count how many different rotate word sets in dictionary.

E.g. picture and turepic are same rotate words.



'''




class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """
    def countRotateWords(self, words):
        if words == []:
            return 0
        # Write your code here
        rotate_words=[words[0]]
        for word1 in words[1:]:
            equal = False
            for word2 in rotate_words:
                if self.compare(word1, word2)==True:
                    equal = True
                    continue
            if equal == False:
                rotate_words.append(word1)
        return len(rotate_words)

    def compare(self, word1, word2):
        equal = False
        if len(word1) != len(word2):
            return equal
        if sum(bytearray(word1, 'utf8')) != sum(bytearray(word2, 'utf8')):
            return equal
        else:
            l = len(word1)
        for i in range(l):
            if word1 == word2[i:]+word2[:i]:
                return True
        return equal
