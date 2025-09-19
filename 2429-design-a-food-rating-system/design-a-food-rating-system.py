class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine = defaultdict(list) # maxHeap -> [(-rating, food)]

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r

            heapq.heappush(self.cuisine[c], (-r, f)) # a separate max heap for each cuisine


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food] # we fetch the cuisine as we have to change the rating
        self.food_to_rating[food] = newRating # set the newRating in the hashmap
        heapq.heappush(self.cuisine[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        maxHeap = self.cuisine[cuisine] # we fetch the maxHeap of that specific cuisine
        while maxHeap:
            rating, food = maxHeap [0] # we fetch the highest rated food from that cuisine
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(maxHeap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)