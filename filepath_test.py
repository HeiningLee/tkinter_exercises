
path = "./data/dataset1.csv"

filehandler = open(path, 'r')
lines = filehandler.readlines()
filehandler.close()
print(lines[0])