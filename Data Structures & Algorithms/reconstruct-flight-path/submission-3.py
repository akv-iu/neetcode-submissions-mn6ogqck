class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dict = collections.defaultdict(list)
        for src,dest in tickets:
            dict[src].append(dest)
        
        n = len(tickets)

        for src in dict:
            dict[src].sort()
        ans = ["JFK"]
        
        def dfs(curr):
            if len(ans) == n+1:
                return True
            for i, dest in enumerate(dict[curr]):
                temp = dict[curr].pop(i)
                ans.append(temp)
                if dfs(dest):
                    return True
                ans.pop()
                dict[curr].insert(i,temp)
            
            return False
        
        if dfs("JFK"):
            return ans
        return -1
                       