class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def again(current, open, close):
            if open == 0 and close == 0:
                result.append(current)
                return
            
            if open > 0:
                again(current + '(', open-1, close)

            if close > open:
                again(current + ')', open, close-1)
        
        again("",n,n)
        return result
                
        