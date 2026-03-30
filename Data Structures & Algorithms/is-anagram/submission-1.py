class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        cmap = {}
        for c in s:
            if c in hmap:
                hmap[c] = hmap[c] + 1
            else:
                hmap[c] = 0
        for c in t:
            if c in cmap:
                cmap[c] = cmap[c] + 1
            else:
                cmap[c] = 0
        if hmap == cmap:
            return True
        else:
            return False       