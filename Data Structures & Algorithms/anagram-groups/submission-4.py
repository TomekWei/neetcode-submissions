class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for arr in strs:
            counts = [0]*26
            for s in arr:
                counts[ord(s)-97] += 1
            key = tuple(counts)
            table[key].append(arr)
        return list(table.values())