class TimeMap:

    def __init__(self):
        self.temp = {} #key:{value, time}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.temp:
            self.temp[key] = []
        self.temp[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.temp:
            return ""
        values = self.temp[key]
        l, r = 0, len(values) -1
        while l <= r:
            mid = (l +r) // 2 
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1 
        return res 

        
