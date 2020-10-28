# initialize my data variable
data = []

# read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
#   data = datafile.read()
    #read the first three lines (header)
    for _ in range(3):
#       print(_)
        datafile.readline()
    # read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)
#debug
#   for datum in data:
#       print(datum)

#print(data[0])
#print(data[9])
#print(data[-1])
#for datum in data[0:10:2]:
#    print(datum)

print(data[8][4])
#print(data[8][4][0])
#print(data[8][:5])
#print(data[8][::2])

