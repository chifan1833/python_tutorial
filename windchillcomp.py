#data = {'date':[], 'time':[], 'tempout':[]}
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

#data types for each column only if non-string
types = {'tempout': float, 'windspeed':float, 'windchill':float}

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
# compute the wind chill temp
def compute_windchill(t, v):
    a =35.74
    b = 0.6215
    c = 35.75
    d = 0.4275
    v16 = v ** 0.16
    wci = a + (b * t) - (c * v16)+ (d * t * v16)
    return wci

#run the function to compure wci
windchill = []
for temp, windspeed in zip(data['tempout'],data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

#print(windchill)
#for wc_data, wc_comp in zip(data['windchill'], windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

# output comparison of data
print('               ORIGINAL   COMPUTED')
print(' DATE   TIME  WINDCHILL  WINDCHILL  DIFFERENCE')
print('------- ----- ---------- ---------- -----------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')



#       data['date'].append(split_line[0])
#       data['time'].append(split_line[1])
#       data['tempout'].append(split_line[2])

#print(data['time'])
#       data['tempout'].append(float(split_line[2]))
#print(data['tempout'])
