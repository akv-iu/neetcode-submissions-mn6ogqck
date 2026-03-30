class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n+1)

        for i in range(n+1):
            j = i
            count = 0
            while i:
                if i%2:
                    count += 1
                i = int(i / 2)
            res[j] = count
        
        return res
        