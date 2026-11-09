class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        
        stable = Counter(s)
        ttable = Counter(t)
        return stable == ttable
