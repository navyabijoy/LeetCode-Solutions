class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}
        color_to_ball = defaultdict(set)
        count = 0
        res = []
        for query in queries:
            ball,color = query
            if ball in ball_to_color: # ball is previously colored
                old_color = ball_to_color[ball] # the prev color
                if old_color == color: # if the prev color matches the current
                    res.append(count) # add the count
                    continue
                

                color_to_ball[old_color].remove(ball) # the prev color does not match color so remove the ball from that dictionary
                if not color_to_ball[old_color]:
                    count -= 1
            
            ball_to_color[ball] = color
            color_to_ball[color].add(ball)

            if len(color_to_ball[color]) == 1: # a color is newly introduced
                count += 1
            res.append(count)
        return res
            
            
