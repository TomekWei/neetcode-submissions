class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdic = sorted((num, i) for i, num in enumerate(nums))
        print(numdic)
        start = 0
        end = len(numdic)-1
        while start < end:
            if numdic[start][0]+ numdic[end][0] == target:
                return sorted([numdic[start][1], numdic[end][1]])
            elif numdic[start][0]+ numdic[end][0] > target:
                end -= 1
            else: start += 1