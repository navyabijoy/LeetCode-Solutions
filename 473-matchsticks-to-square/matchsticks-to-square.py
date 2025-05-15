class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4 or sum(matchsticks) % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        side = sum(matchsticks) // 4
        for m in matchsticks:
            if m > side:
                return False
        track = [0,0,0,0]
        n = len(matchsticks)
        
        def backtrack(curr,track):
            if curr == n:
                return (i == side for i in track)
            for i in range(4):
                if track[i] + matchsticks[curr] <= side:
                    track[i] += matchsticks[curr]
                    if (backtrack(curr+1,track)):
                        return True
                    track[i] -= matchsticks[curr]
            return False
            
        return backtrack(0,track)


