class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = [[value, timestamp]]
        else:
            self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keyStore:
            return ""

        arr = self.keyStore[key]
        
        r = len(arr) - 1
        l = 0

        res = ""
        while l <= r:
            m = ((r - l) // 2) + l
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
