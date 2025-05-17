from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        used = [False] * len(strs)
        
        for i in range(len(strs)):
            if not used[i]:
                group = [strs[i]]
                used[i] = True
                for j in range(i + 1, len(strs)):
                    if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                        used[j] = True
                new_strs.append(group)
                    
        return new_strs

strs = ["act","pots","tops","cat","stop","hat"]
sol = Solution()
print(sol.groupAnagrams(strs))

strs = ["x"]
sol = Solution()
print(sol.groupAnagrams(strs))

strs = [""]
sol = Solution()
print(sol.groupAnagrams(strs))
