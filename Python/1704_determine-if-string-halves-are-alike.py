class Solution:
    VOWELS = set('aeiou')

    def halvesAreAlike(self, s: str) -> bool:
        vowel_count = 0

        for idx in range(0, len(s) // 2):
            char = s[idx].lower()
            vowel_count += char in self.VOWELS

        for idx in range(len(s) // 2, len(s)):
            char = s[idx].lower()
            vowel_count -= char in self.VOWELS

        return vowel_count == 0
