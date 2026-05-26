class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        hash = {}
        for word in strs:
            ans = [0 for i in range(26)]
            for char in word:
                pos = ord(char) - ord('a')
                ans[pos] += 1
            ans = tuple(ans)
            if ans in hash:
                hash[ans].append(word)
            else:
                hash[ans] = [word]

        print(list(hash.values()))  
        
        
        return list(hash.values())
        