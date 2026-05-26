class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        final = {i:[] for i in range(len(nums)+1)}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        print(hash)
        for key in hash:
            final[hash[key]].append(key)
        print(final)
        ans = []
        for i in range(len(final) - 1, -1, -1):
    
            for num in final[i]:
                ans.append(num)
                
                if len(ans) == k:
                    return ans

        
        return []