class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        

        def count(arr) -> dict:
            hash = defaultdict()
            for i in arr:
                if i in hash:
                    hash[i]+= 1
                else:
                    hash[i] = 1
            return hash
        
        hash_s = count(s)
        hash_t = count(t)

        if hash_s == hash_t:
            return True
        return False
