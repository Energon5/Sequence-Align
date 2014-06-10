import pandas as pd
io = pd.read_csv('gongcsv.csv', sep=",", usecols=(0,))
iolist = map(list, io.values)
print iolist[0]
for nums in iolist:
	print nums
#csv = open('gongcsv.csv', 'r')
#csv.readline().split()
#print csv
