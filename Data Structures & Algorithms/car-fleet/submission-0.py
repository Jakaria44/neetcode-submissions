class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        posToSpd = {}

        for i in range(len(position)):
            posToSpd[position[i]]= speed[i]

        count = 0
        time = 0
        for curr in sorted(position, reverse=True):
            arrival = (target-curr)/posToSpd[curr]

            if arrival > time:
                count+=1
                time= arrival

        return count
