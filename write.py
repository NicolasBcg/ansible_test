import sys

def main(filename,line):
    fichier = open(filename, "a")
    fichier.write(line)
    fichier.close()

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
