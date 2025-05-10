# s = "racecar" 
# t = "carrace"

s = "jar" 
t = "jam"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1_sorted = sorted(s)
        str1 = "".join(sorted(str1_sorted))
        str2_sorted = sorted(t)
        str2 = "".join(sorted(str2_sorted))
        if str1 == str2:
            return True

sol = Solution()
print(sol.isAnagram(s, t))
