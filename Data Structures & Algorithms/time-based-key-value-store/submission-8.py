class TimeMap:

    def __init__(self):
        self.temp = {} #key:[value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.temp:
            self.temp[key] = []
        self.temp[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.temp:
            return ""
        values = self.temp[key]
        #1, 2, 4, 5 timestamp = 3
        l = 0 
        r = len(values) -1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m +1
            else:
                r = m-1
        return res 

        
