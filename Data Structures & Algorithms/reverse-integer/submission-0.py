class Solution:
    def reverse(self, x: int) -> int:
        
        MIN = -2147483648
        MAX = 2147483648

        res = 0
        while x:
            # get the last digit, cut it off
            last = int(math.fmod(x, 10))
            x = int(x / 10)

            # check to make sure x is not out of bounds
            if (res > MAX // 10 or (res == MAX // 10 and last > MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and last < MIN % 10)):
                return 0

            # add last to res
            res = (res * 10) + last

        return res