# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        count = 0
        
        for left in range(n):
            vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
            for right in range(left, n):
                if word[right] in vowels:
                    vowels[word[right]] += 1
                    if all(vowels[vowel] > 0 for vowel in 'aeiou'):
                        count += 1
                else:
                    break

        return count