class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # with hashmap

        count = defaultdict(int)
        for val in hand:
            count[val] += 1
        
        for i in range(len(hand)):
            num = hand[i]
            if count[num] == 0:
                continue
            start = num
            while count[start] > 0:
                start -= 1
            
            start += 1
            for j in range(start, start + groupSize):
                if count[j] == 0:
                    print(j)
                    return False
                count[j] -= 1

        return True