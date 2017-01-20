def findMatches (motif1, motif2):
	import pandas as pd

	#Initializing the file to two variables for each motif
	motif1read = pd.read_csv(motif1, sep=",", usecols=(0,))
	motif2read = pd.read_csv(motif2, sep=",", usecols=(0,))

	#Mapping those to lists
	m1list = map(list, motif1read.values)
	m2list = map(list, motif2read.values)

	#Getting the columns that contain the name of the motif
	motif1names = pd.read_csv(motif1, sep=",", usecols=(4,))
	motif2names = pd.read_csv(motif2, sep=",", usecols=(4,))

	#Mapping the motif names to lists
	m1nlist = map(list, motif1names.values)
	m2nlist = map(list, motif2names.values)

	#Variables to be filled
	motif1match = ""
	motif2match = ""
	motifmatch = ""
	m1m2match = 0
	m1m2name = 0
	already_seen = set()
	#Looping through the lists. Then get comparison percentage?
	for index, i in enumerate(m1list):
		motif1match = str(i)
		motif1match = motif1match.strip('[]')
		motif1match = motif1match.translate(None, "'")
		m1name = str(m1nlist[index])
		moutput = open(i + ".txt", "wb")
		for index, j in enumerate(m2list):
			motif2match = str(j)
			motif2match = motif2match.strip('[]')
			motif2match = motif2match.translate(None, "'")
			m2name = str(m2nlist[index])		
			if motif1match.endswith("Dup1") or motif1match.endswith("Dup2") or motif1match.endswith("Dup3") or motif1match.endswith("Dup4") or motif1match.endswith("Dup10") or motif1match.endswith("Dup9") or motif1match.endswith("Dup8") or motif1match.endswith("Dup7") or motif1match.endswith("Dup6") or motif1match.endswith("Dup5"):
				#continue
			if motif1match == motif2match:
				moutput.write("Found match " + motif1match + " with " + motif2match + "\n")
				#already_seen.add(motif1match)
				m1m2match += 1				
	#pertotal = m1m2match/524.0*100
	#print pertotal
	#pertotal = str(pertotal)
	#moutput.write("Found " + str(m1m2match) + " total matches out of 524 sequences total = " + pertotal + " percent of total sequences.")

tomatch1 = raw_input("Please enter first file to match: ")
tomatch2 = raw_input("Please enter second file: ")
findMatches(tomatch1,tomatch2)
