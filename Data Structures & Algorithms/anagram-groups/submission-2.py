class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        i = 0

        for arr in strs:
            counts = [0]*26
            for s in arr:
                counts[ord(s)-97] += 1
            key = str(counts)
            if key not in table:
                table[key] = [arr]
            else:
                table[key].append(arr)
        return list(table.values())