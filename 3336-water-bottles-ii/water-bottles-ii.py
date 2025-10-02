class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            count += 1
            empty = empty - numExchange + 1
            numExchange += 1 
            
        return count