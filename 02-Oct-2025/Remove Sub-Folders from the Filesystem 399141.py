# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        f = sorted(folder)
        n = len(f)
        res = [f[0]]
        
        for i in range(1, n):
            if not f[i].startswith(res[-1] + "/"):
                res.append(f[i])      
        return res