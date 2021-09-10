class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for idx in range(1, n + 1):
            answer = (idx % 3 == 0) * 'Fizz' + (idx % 5 == 0) * 'Buzz'
            answer = answer if answer else str(idx)
            result.append(answer)

        return result
