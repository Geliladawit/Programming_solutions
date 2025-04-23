# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        st = ["main"]
        for i in logs:
            if i == "../" and len(st) > 1:
                st.pop()
            elif i == "./":
                continue
            elif i != "./" and i != "../":
                st.append(i)
        return len(st) - 1