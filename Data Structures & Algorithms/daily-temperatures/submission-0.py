class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        holder = []   
        n = len(temperatures)
        ans = [0] * n
        if  n == 1:
            return 0

        for i in range(n):
            if i == 0:
                stack.append([temperatures[0],0])
                print(stack[-1][0])

            elif not stack or temperatures[i] < stack[-1][0]:
                stack.append([temperatures[i],i])
            else:
                print(stack)
                
                while(stack and temperatures[i]>stack[-1][0]):
                    holder.append(stack.pop())
                    ans[holder[0][1]] = i - holder[0][1]
                    holder.pop()
                stack.append([temperatures[i],i])
                

        return ans 



        