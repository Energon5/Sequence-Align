import pandas as pd
io = pd.read_csv('gongcsv.csv', sep=",", usecols=(0,))
print io
#csv = open('gongcsv.csv', 'r')
#csv.readline().split()
#print csv
