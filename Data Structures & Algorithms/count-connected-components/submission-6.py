class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hash = {i:[] for i in range(n)}
        for curr,next in edges:
            hash[curr].append(next)
            hash[next].append(curr)
        visit = set()
        count = 0
        print(hash)

        
        
        def dfs(node):
            visit.add(node)
            if hash[node] == []:
                return
            
            for next in hash[node]:
                if next not in visit:
                    print(f"next ={next}")
                    dfs(next)

        for i in range(len(hash)):
            if i not in visit:
                print(f"i = {i}")
                count += 1
                dfs(i)    
        return count