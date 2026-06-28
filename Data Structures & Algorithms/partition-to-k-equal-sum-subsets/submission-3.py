class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        parts = [[] for _ in range(k)]
        total = sum(nums)
        subTotal = total // k

        if total % k != 0:
            return False

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        nums.sort(reverse = True)

        # i is nums index
        # j is parts index
        def partition(j):
            if j >= k:
                return True
            if sum(parts[j]) == subTotal:
                return partition(j + 1)
            
            for num in count.keys():
                if count[num] > 0 and sum(parts[j]) + num <= subTotal:
                    parts[j].append(num)
                    count[num] -= 1

                    if partition(j):
                        return True

                    parts[j].pop()
                    count[num] += 1
                else:
                    continue
            
            return False

        return partition(0)