import pandas as pd
from Bio import SeqIO

#Initialize SeqIO object with Tomato Genome
tomdict = SeqIO.index("tomgenome.fa", "fasta")

#Open GFF file converted to CSV for gene id locations, as well as initialize a list from the values
locations = pd.read_csv("TomatoLocations.csv", sep=",", usecols=(9,))
locationlist = map(list,locations.values)

#Initialize two more openings of the GFF file for the chromosome, and start position of sequence
chromloc = pd.read_csv("TomatoLocations.csv", sep=",", usecols=(0,))
startloc = pd.read_csv("TomatoLocations.csv", sep=",", usecols=(3,))

#Initialize both of them to a list from their values
chromloclist = map(list, chromloc.values)
startlist = map(list, startloc.values)

#Opens the file with the list of genes to pull from the genome
genelocations = pd.read_csv("replacedgenes.csv", sep=",", usecols=(0,))
geneloclist = map(list, genelocations.values)

#Initializing values before needed in the loop
names = ""
locationstr = ""
chromlocation = ""
startlocation = ""

sequence = ""
pulledseq = ""

#Open the file to write to
writefile = open("upstreamseqs30m2.fasta", "wb")

#First loop to loop through the list containing our gene ID's first
for i in geneloclist:
	names = str(i)
	names = names.strip('[]')
	names = names.translate(None, "'")
	#print i
#Second Loop to go through the main GFF file
	for index, j in enumerate(locationlist):
		locationstr = str(j)
		locationstr = locationstr.strip('[]')
		locationstr = locationstr.translate(None, "'")
		#print names + " " + locationstr
		#If to check if the gene ID from our list matches the GFF file Name. This if then strips all strings of unnecessary [], and '' tags, and converts the start location to an int in order to access them in the seq file. Then writes it to a seq fasta file for all the sequences. **Needs to be generalized more.
		if locationstr == "Name=" + names:
			print "Found: " + locationstr
			chromlocation = str(chromloclist[index])
			chromlocation = chromlocation.strip('[]')
			chromlocation = chromlocation.translate(None,"'")
			startlocation = str(startlist[index])
			startlocation = startlocation.strip('[]')
			startlocation = startlocation.translate(None,"'")
			startlocation = float(startlocation)
			startlocation = int(startlocation)
			sequence = tomdict[chromlocation].seq
			pulledseq = sequence[startlocation-3000:startlocation]
			writefile.write(">" + locationstr + "\n" + str(pulledseq) + "\n")
writefile.close()

