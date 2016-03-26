import pickle

FILE_NAME = "store.pickle"

class PickleStore():
    def __init__(self):
        self.store = []

    def make_file(self):
        with open(FILE_NAME, "w") as f:
            pickle.dump(self.store, f)

    def load(self):
        with open(FILE_NAME, "r") as f:
            self.store = pickle.load(f)

    def save(self):
        with open(FILE_NAME, "w") as f:
            pickle.dump(self.store, f)
            
    def add_item(self, item):
        with open(FILE_NAME, "r") as f:
            self.store = pickle.load(f)
            self.store.append(item)
        self.save()

    def get(self):
        return self.store
