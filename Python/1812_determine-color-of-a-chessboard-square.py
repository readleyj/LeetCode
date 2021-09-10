class Solution:
    def get_alphabet_pos(self, char):
        return ord(char) - 96

    def squareIsWhite(self, coordinates: str) -> bool:
        coord_sum = self.get_alphabet_pos(coordinates[0]) + int(coordinates[1])

        return coord_sum % 2 == 1
