import sys
import os
def main(model,nom,date,config):
    path="backupsMicrotiks"
    if os.path.exists(path) == False:
        os.mkdir(path)
    path+="/"+model
    if os.path.exists(path) == False:
        os.mkdir(path)

    filename=path+"/"+nom+date+".cfg"
    fichier = open(filename, "w")
    fichier.write(config)
    fichier.close()

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
