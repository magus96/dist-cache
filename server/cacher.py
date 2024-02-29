import Pyro4

@Pyro4.expose
class Cacher:
    def __init__(self):
        self.cache = {}
    
    def set(self, key, value):
        self.cache[key] = value

    def get(self, key):
        value = self.cache.get(key)
        if value is None:
            print("Cache miss")
        else:
            print("Cache hit")
        
        return value