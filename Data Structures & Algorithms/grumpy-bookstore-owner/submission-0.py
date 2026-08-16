class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)

        window_gain = 0
        best_gain = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                window_gain += customers[i]
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    window_gain -= customers[i - minutes]
            best_gain = max(best_gain, window_gain)

        return base + best_gain