class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        # Total number of even positions
        even_positions = (n + 1) // 2
        # Total number of odd positions
        odd_positions = n // 2
        
        # Calculate (5^even_positions) % MOD and (4^odd_positions) % MOD
        even_power = pow(5, even_positions, MOD)
        odd_power = pow(4, odd_positions, MOD)
        
        # Return the product modulo MOD
        return (even_power * odd_power) % MOD
            