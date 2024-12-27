class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        size = len(cardPoints)
        left, right = k-1, size-1
        
        # Initial pick: take all k card from left hand side
        current_pick = sum(cardPoints[:k])
        max_point = current_pick
        
        # adjustment
        for _ in range(k):
            
            # left hand side discards one, and right hand side picks one more 
            current_pick += ( cardPoints[right] - cardPoints[left] )
            
            # update max point
            max_point = max(max_point, current_pick)
            
            # update card index for both sides in adjustment
            left, right = left-1, right-1
            
        return max_point