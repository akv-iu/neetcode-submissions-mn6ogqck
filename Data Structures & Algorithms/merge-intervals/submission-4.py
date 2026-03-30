class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Edge case for empty lists
        if not intervals:
            return []
            
        res = []
        i = 0
        n = len(intervals) - 1
        intervals.sort()

        # Wrap everything in one main loop to handle multiple clusters
        while i <= n:
            
            # Your exact logic for merging a cluster
            while i < n and intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
                i += 1
            
            # Once the inner loop stops, we've finished a cluster. Append it.
            res.append(intervals[i])
            i += 1
            
        return res