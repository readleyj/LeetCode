class Solution:
    def sum_digits(self, num):
        digit_sum = 0

        while num:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball_counts = Counter()
        max_num_balls = -1

        for num in range(lowLimit, highLimit + 1):
            digit_sum = self.sum_digits(num)

            ball_counts[digit_sum] += 1

            max_num_balls = max(max_num_balls, ball_counts[digit_sum])

        return max_num_balls
