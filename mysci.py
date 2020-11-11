#data = {'date':[], 'time':[], 'tempout':[]}
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7}

#data types for each column only if non-string
types = {'tempout': float, 'windspeed':float}

data = {}
for column in columns:
    data[column] = []

filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    for _ in range(3):
        headerline = datafile.readline()

    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

#       data['date'].append(split_line[0])
#       data['time'].append(split_line[1])
#       data['tempout'].append(split_line[2])

#print(data['time'])
#       data['tempout'].append(float(split_line[2]))
print(data['tempout'])
