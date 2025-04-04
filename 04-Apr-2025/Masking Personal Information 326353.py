# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = str(s) 
        if "@" in s:
            s = s.lower()
            n, d = s.split("@")
            masked_name = n[0] + "*" * 5 + n[-1]
            s = masked_name + "@" + d
        else:
            digits = ''.join(filter(lambda x: x.isdigit(), s))
            masked_number = "***-***-" + digits[-4:]
            if len(digits) > 10:
                masked_number = "+" + "*" * (len(digits) - 10) + "-" + masked_number
            s = masked_number
            
        return s
