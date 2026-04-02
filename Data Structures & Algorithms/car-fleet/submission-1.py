class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        for i in range(len(position)):
            times = (target-position[i])/speed[i]
            time[position[i]] = times

        position.sort(reverse=True)
        timestack = []
        fleet = 1
        for i in position:
            if len(timestack) == 0:
                timestack.append(time[i])
            elif timestack[-1] >= time[i]:
                continue
            else:
                fleet  += 1
                timestack.append(time[i])
        return fleet 

        