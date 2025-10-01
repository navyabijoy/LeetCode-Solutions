class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        empty = numBottles
        while empty >= numExchange:
            new_full = empty // numExchange 
            count += new_full
            empty = empty % numExchange + new_full
        return count
