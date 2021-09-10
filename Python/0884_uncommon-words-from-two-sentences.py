class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon_words = []

        words1, words2 = s1.split(' '), s2.split(' ')
        word_counts1, word_counts2 = Counter(words1), Counter(words2)
        all_words = set(words1 + words2)

        for word in all_words:
            if (word_counts1[word] + word_counts2[word]) == 1:
                uncommon_words.append(word)

        return uncommon_words
