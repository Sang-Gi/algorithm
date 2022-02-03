class LInkedTuple:
    def __init__(self):
        self.items = list()
    
    # [("ksdfksdf8", "test")] -> [("ksdfksdfk", "test2")]
    def add(self, key, value):
        self.items.appned(key, value)
    
    # .add("ksdfksdf8", "test")
    # [("ksdfksdf8", "test")]
    # .add("ksdfksdfk", "test2")
    # [("ksdfksdf8", "test"), [("ksdfksdfk", "test2")]] 
    
    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = [] # [LInkedTuple(), LInkedTuple() ...]
        for i in range(8):
            self.items.append(LInkedTuple())

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        self.items[idx].add(key, value)


    def get(self, key):
        idx = hash(key) % len(self.items)

        return self.items[idx].get(key)
