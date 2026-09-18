class TimeMap:

    def __init__(self):
        self.temp = {} #stroing (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.temp:
            self.temp[key] = []
        self.temp[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.temp:
            return ""
        value = self.temp[key]
        l, r = 0, len(value)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if value[m][1] < timestamp:
                res = value[m][0]
                l = m + 1
            elif value[m][1] > timestamp:
                r = m -1
            else:
                return value[m][0]
        return res


        
