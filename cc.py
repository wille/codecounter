import argparse
import os

argparse = argparse.ArgumentParser()
argparse.add_argument("-d", "--dir", dest = "dir")

args = argparse.parse_args()

global folder
folder = args.dir or "."

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
    
    print("Complete")