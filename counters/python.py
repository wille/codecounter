from .counter import Counter

class Python(Counter):
    def count(self):
        print("overridden")
        
    def extensions(self):
        return [ "py" ]