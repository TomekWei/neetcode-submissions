class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        stable = Counter(s)
        ttable = Counter(t)
        return stable == ttable
