class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dict = {i:[] for i,j in tickets}
        n = len(tickets)
        print(n)
        ans = []
        for i,j in tickets:
            dict[i].append(j)
        print(dict)
        
        def dfs(src,dest,count):
            count += 1
            print(count)
            print(dest)
            ans.append(src)

            if count == n+1:
                print(ans)
                return True
            else:
                ans.pop()
                count -= 1
                return -1
            
            
            
            for destinations in dict[dest].copy():
                temp = dict[dest].pop(0)
                if dfs(dest,destinations,count) ==0: 
                    return 0
                dict[dest].append(temp)
                continue
            
            return -1
        
        for dest in dict["JFK"]:
            final = dfs("JFK",dest,1)
        return ans
        