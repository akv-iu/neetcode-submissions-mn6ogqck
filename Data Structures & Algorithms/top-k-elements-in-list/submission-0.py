from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range(len(nums)+1)]
        count = {}
        final = []
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
            print(count)

        for n,c in count.items():
            res[c].append(n)
        print(res)
        
        for i in range(len(res)-1,0,-1):
            for n in res[i]:
                final.append(n)
                if len(final) == k:
                    return final



