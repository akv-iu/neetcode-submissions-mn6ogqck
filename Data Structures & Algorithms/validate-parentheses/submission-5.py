class Solution:
    def isValid(self, s: str) -> bool:
        bracmap = {'}':'{', ']':'[', ')':'(' }
        stc = []
        isempty = not bool(s)
        if isempty:
            return False


        for i in s:
            
            if i in bracmap:
                if stc and bracmap[i] == stc[-1]:
                    stc.pop()
                else:
                    return False
            else:
                stc.append(i)
                
            
        
        return True if not stc else False

        