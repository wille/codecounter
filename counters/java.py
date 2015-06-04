from .counter import Counter

class Java(Counter):
    
    def count(self, lines):
        total = 0
        sloc = 0;
        
        for line in lines:
            total += 1
            if self.is_valid(line):
                sloc += 1
            
        return total, sloc
    
    def is_valid(self, line):
        line = line.strip()
        return not line.startswith("//") and not line.startswith("/*") and not line.startswith("/**") and not "*/" in line and not line == "*" and len(line) > 0
        
    def extensions(self):
        return [ "java" ]