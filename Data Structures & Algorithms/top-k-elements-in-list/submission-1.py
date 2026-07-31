class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for item in nums:
            frequency[item] = 1 + frequency.get(item,0)
        for key ,value in frequency.items():
            bucket[value].append(key)
        res = []
        for freq in range(len(bucket)-1,0,-1):
            for item in bucket[freq]:
                res.append(item)
                if len(res) == k:
                    return res
        