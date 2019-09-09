class HashMap:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0

        for val in str(key):
            hash += ord(val)
        return hash % self.size
