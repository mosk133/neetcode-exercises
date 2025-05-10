class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        if str1 == str2:
            return True
        return False

s = "racecar" 
t = "carrace"

sol = Solution()
print(sol.isAnagram(s, t))

s = "jar" 
t = "jam"

print(sol.isAnagram(s, t))
