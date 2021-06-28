class Solution:
    def calc_sum(self, word):
        return int(''.join(str(ord(char) - 97) for char in word))

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.calc_sum(targetWord) == (self.calc_sum(firstWord) + self.calc_sum(secondWord))
