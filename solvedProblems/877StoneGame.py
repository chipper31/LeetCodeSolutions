class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        # There is an odd number of stones so there is
        # never a tie. There is an even number of piles
        # so alice can always choose if she gets all the
        # piles at even or odd indicies. Which ever group
        # has a higher total she will take. Alice always
        # has a winning strategy
        return True