class Solution:
    def count_digit_sum(self, n):
        digit_sum = 0

        while n:
            digit_sum += n % 10
            n //= 10

        return digit_sum

    def countLargestGroup(self, n: int) -> int:
        sum_counter = Counter()

        for num in range(1, n + 1):
            digit_sum = self.count_digit_sum(num)

            if digit_sum not in sum_counter:
                sum_counter[digit_sum] = 0

            sum_counter[digit_sum] += 1

        digit_sums = list(sum_counter.values())
        return digit_sums.count(max(digit_sums))
