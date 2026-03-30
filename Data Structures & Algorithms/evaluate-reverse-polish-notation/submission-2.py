class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opMap = {'+','-','*', '/'}
        load = []

        def math(left, right, operator):
            if operator == '+':
                return (left + right)
            elif operator == '-':
                return (left - right)
            elif operator == '*':
                return (left * right)
            else:
                return (int(left / right))
        
        for i in tokens:
            if i in opMap:
                right = load.pop()
                left = load.pop()
                ans = math(left,right,i)
                load.append(ans)
            else:
                load.append(int(i))
        return(load.pop())
            