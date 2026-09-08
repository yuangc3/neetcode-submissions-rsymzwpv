class TimeMap:

    def __init__(self):
        self.temp = {} #store[value. timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.temp:
            self.temp[key] = []
        self.temp[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.temp:
            return ""
        values = self.temp[key] #[value, timestamp]
        l, r = 0, len(values)-1
        res = ""
        while l <= r:
            mid = (l+r) //2
            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                return values[mid][0]
        return res
                
            


        
