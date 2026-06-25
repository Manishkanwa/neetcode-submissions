class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        final = []
        for num in nums:
            if num in map.keys():
                map[num] += 1
            else:
                map[num] = 1
        map = sorted(map.items(), key = lambda item: item[1], reverse = True)
        for i in range(0,k):
            final.append(map[i][0])
        return final