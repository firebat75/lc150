class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2, t2 = [*s], [*t]
        s2.sort()
        t2.sort()

        return s2 == t2
