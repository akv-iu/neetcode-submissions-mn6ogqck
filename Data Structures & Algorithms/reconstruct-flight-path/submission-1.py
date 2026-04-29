import collections

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # 1. Build the graph safely using defaultdict
        graph = collections.defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        
        # 2. Sort destinations so we always try the lexicographically smallest first
        for src in graph:
            graph[src].sort()
            
        n = len(tickets)
        ans = ["JFK"] # We always start at JFK, so we can initialize it here
        
        # 3. Simplified DFS that only needs to know where we currently are
        def dfs(curr):
            # Base Case: Did we use all the tickets?
            if len(ans) == n + 1:
                return True
            
            # 4. Use enumerate to safely get the index and the destination
            for i, next_dest in enumerate(graph[curr]):
                
                # Take the ticket out (mark as used) and add to our path
                graph[curr].pop(i)
                ans.append(next_dest)
                
                # Dive deep! If it eventually returns True, we bubble that True all the way up
                if dfs(next_dest):
                    return True
                
                # Backtrack: If we hit a dead end, pop it off the answer...
                ans.pop()
                # ...and put the ticket exactly back where we found it
                graph[curr].insert(i, next_dest)
                
            # If we run out of options and haven't hit the base case, this path is a dead end
            return False

        # Kick off the search
        dfs("JFK")
        
        return ans