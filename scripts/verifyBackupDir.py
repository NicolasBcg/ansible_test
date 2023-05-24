import sys
import os

def main(model):
    path="/home/ansible/backupsMicrotiks"
    if os.path.exists(path) == False:
        os.mkdir(path)
    path+="/"+model
    if os.path.exists(path) == False:
        os.mkdir(path)   
    
if __name__ == "__main__":
    main(sys.argv[1])
