class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        i = 0
        result = []
        for arr in strs:
            counts = [0]*26
            for s in arr:
                counts[ord(s)-97] += 1
            if str(counts) not in table:
                table[str(counts)] = i
                result.append([arr])
                i+=1
            else:
                result[table[str(counts)]].append(arr)
        return result