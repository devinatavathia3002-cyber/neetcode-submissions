class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0

        for _ in range(32):
            reversed_n = reversed_n << 1
            last = n & 1
            n = n >> 1
            reversed_n = reversed_n | last

        return reversed_n