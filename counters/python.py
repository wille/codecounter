from .counter import Counter

class Python(Counter):
    
    def count(self, lines):
        total = 0
        sloc = 0;
        
        for line in lines:
            total += 1
            if self.is_valid(line):
                sloc += 1
            
        return total, sloc
    
    def is_valid(self, line):
        return True
        
    def extensions(self):
        return [ "py" ]