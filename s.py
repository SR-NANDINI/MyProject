class Solution:
    def winnerSquareGame(self, n):
        # Intuition: plain recursive minimax, Alice maximizes, Bob minimizes, no caching
        return self.game(n, True)

    def game(self, n, isAlice):
        if n == 0:
            return not isAlice
        i = 1
        while i * i <= n:
            if isAlice:
                if self.game(n - i * i, False):
                    return True
            else:
                if not self.game(n - i * i, True):
                    return False
            i += 1
        return not isAlice