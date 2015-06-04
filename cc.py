import argparse
import os
import re
from counters import *
from counters import modules
import sys
import os.path

argparse = argparse.ArgumentParser()
argparse.add_argument("-d", "--dir", dest = "dir")
argparse.add_argument("-e", "--extension", dest = "extension")
argparse.add_argument("-v", "--verbose", action = "store_true")

args = argparse.parse_args()

global folder
folder = args.dir or "."

global extension
extension = args.extension or "."

global verbose
verbose = args.verbose

def index(source):
    list = []
    
    for root, dirs, files in os.walk(source):
        relroot = os.path.abspath(os.path.join(source))
        dir = os.path.relpath(root, relroot)

        for file in files:
            filename = os.path.join(root, file)

            if os.path.isfile(filename):
                relative = os.path.join(os.path.relpath(root, relroot), file)      

                if folder is "." and relative.startswith("." + os.sep):
                    relative = relative[2:]

                for m in modules:
                    module = m()
                    for ext in module.extensions():
                        if relative.endswith(ext):
                            list.append([relative, module])                    
                
    return list

if __name__ == "__main__":
    print("Starting codecounter")
    
    totallines = 0
    totalsloc = 0
    
    print("Indexing " + folder + "...")
    
    list = index(folder)
    
    print("Counting " + str(len(list)) + " files...")
        
    for file, module in list:
        file = folder + os.sep + file

        try:
            if os.path.isfile(file):
                with open(file) as f:                        
                    total, sloc = module.count(f.readlines())
                    totallines += total
                    totalsloc += sloc
                    
                    if verbose:
                        print(file + ", Total: " + str(total) + ", SLOC: " + str(sloc))
        except:
            pass       

    print("Total lines: " + str(totallines))       
    print("Total sloc: " + str(totalsloc))
    
    p = round((totalsloc / totallines) * 100, 2)
    print("Actual code: " + str(p) + "%")
        
    print("Complete")