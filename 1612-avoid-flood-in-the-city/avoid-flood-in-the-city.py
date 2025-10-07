class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        sunny_days = SortedList()
        full_lakes = {} # lake -> the day it got full

        for i, rain in enumerate(rains):
            if rain == 0: # dry day
                sunny_days.add(i) # add the index of sunny day
                continue # move to the next day
            
            # if its not a dry day
            if rain in full_lakes: # if that lake is already full
                last_rain_day = full_lakes[rain]
                idx = sunny_days.bisect_right(last_rain_day)

                if idx == len(sunny_days):
                    return [] # no available sunny day
                
                dry_day = sunny_days[idx]
                ans[dry_day] = rain
                sunny_days.remove(dry_day)
            
            ans[i] = -1
            full_lakes[rain] = i
            
        return ans