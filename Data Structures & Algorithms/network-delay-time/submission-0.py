class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        hash = {i:[] for i in range(1,n+1)}
        for i,j,k in times:
            hash[i].append([j,k])
        print(hash)

        def dfs(start,count,ans):
            count+= 1
            print(ans)
            if count == n:
                # visit.remove(start) Not required as we moved count up
                return ans
            if hash[start] == []:
                return -1
            visit.add(start)
            
            for dest,time in (hash[start]):
                print(start,dest,time,count)
                if dest not in visit:
                    if dfs(dest,count,ans+time) == -1:
                        return -1
            visit.remove(start)
            return ans
        start_ans = 10000
        for i in range(len(times)):
            if times[i][0] == k:
                ans = dfs(times[i][0],0,0)
                if ans != -1:
                    start_ans = min(ans,start_ans)
        
        if start_ans == 10000:
            return -1
        return start_ans
