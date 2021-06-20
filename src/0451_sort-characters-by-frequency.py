# Sorting solution
class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = Counter(s)
        return sorted(s, key=lambda char: (frequencies[char], ord(char)), reverse=True)
