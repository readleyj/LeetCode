class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        goat_words = []

        for idx, word in enumerate(words):
            output = word

            if word[0].lower() not in self.VOWELS:
                output = output[1:] + output[0]

            output += 'ma' + 'a' * (idx + 1)
            goat_words.append(output)

        return ' '.join(goat_words)
