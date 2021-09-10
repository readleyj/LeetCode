class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_set = Counter(chars)

        result = 0
        for word in words:
            word_char_count = Counter(word)

            if all([word_char_count[char] <= char_set[char] for char in word]):
                result += len(word)

        return result
