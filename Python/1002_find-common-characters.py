class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_counters = []
        result = []

        for word in words:
            char_counters.append(Counter(word))

        for char in set(words[0]):
            char_counts = [counter[char] for counter in char_counters]
            result.extend(min(char_counts) * [char])

        return result
