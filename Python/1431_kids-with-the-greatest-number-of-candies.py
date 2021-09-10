class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        return [num_candies + extraCandies >= max_candies for num_candies in candies]
