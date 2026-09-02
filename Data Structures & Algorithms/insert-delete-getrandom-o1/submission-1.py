import random
class RandomizedSet:

    def __init__(self):
        self.temp = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.temp:
            self.temp.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.temp:
            self.temp.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        random_value = random.choice(list(self.temp))
        return random_value

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()