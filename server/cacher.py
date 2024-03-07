import Pyro4
CACHE_LEN = 16

@Pyro4.expose
class Cacher:
    def __init__(self):
        self.cache = {}
        self.eles = []
    
    def set(self, key, value):
        self.cache[key] = value
        if len(self.eles) > 16:
            del self.cache[self.eles[0]]
            self.eles.pop(0)
            self.eles.append(key)
        self.eles.append(key)

    def get(self, key):
        value = self.cache.get(key)
        if value is None:
            print("Cache miss")
        else:
            print("Cache hit")
        
        return value