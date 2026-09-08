class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i,0)
        
        arr = [[] for i in range(len(nums)+1)]

        for num in freq:
            index = freq[num]
            arr[index].append(num)
        
        ans = []

        for i in range(len(arr)-1,0,-1):
            if arr[i] ==[]:
                continue
            else:
                ans += arr[i] 
                if len(ans) >=k:
                    return ans[:k]

        