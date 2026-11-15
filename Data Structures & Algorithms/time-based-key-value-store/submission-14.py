class TimeMap:

    def __init__(self):
        self.temp = defaultdict(list) #storing [value, time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.temp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.temp:
            return ""
        value = self.temp[key]
        l, r = 0, len(value)-1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            if value[mid][1] < timestamp:
                res = value[mid][0]
                l = mid + 1
            elif value[mid][1] > timestamp:
                r = mid - 1
            else:
                return value[mid][0]
        return res 

        
