class Solution:
    MORSE_MAPPING = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
        "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]

    def transform_morse(self, word):
        morse = ''

        for letter in word:
            morse += self.MORSE_MAPPING[ord(letter) - 97]

        return morse

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations = set()

        for word in words:
            transformations.add(self.transform_morse(word))

        return len(transformations)
