import argparse
import os
import re

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

                list.append(relative)
                
    return list

if __name__ == "__main__":
    print("Starting codecounter")
    
    list = index(folder)
        
    for file in list:
        if file.endswith(extension):
            with open(file) as f:
                print(file);
                flines = len(f.readlines())
                print(flines)
    
    print("Complete")