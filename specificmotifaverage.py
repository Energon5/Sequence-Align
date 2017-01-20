import pandas as pd
def find_matches (motif1, motif2, nummotifs):

    # Initializing the file to two variables for each motif
    motif1read = pd.read_csv(motif1, sep=",", usecols=(0,))
    motif2read = pd.read_csv(motif2, sep=",", usecols=(0,))

    # Mapping those to lists
    m1list = map(list, motif1read.values)
    m2list = map(list, motif2read.values)

    # Getting the column that contains the name of the motif
    motif2names = pd.read_csv(motif2, sep=",", usecols=(4,))

    # Mapping the motif names to list
    m2nlist = map(list, motif2names.values)

    # Variables to be filled, and opening a file to store averages
    nummotifs = int(nummotifs)
    motif1match = ""
    motif2match = ""
    motifmatch = ""
    m1m2match = 0
    average = 0
    avfile = open("averages.txt", "wb")
    # Looping through the lists. Opens files to store for each value.
    for index, i in enumerate(m1list):
        motif1match = str(i)
        motif1match = motif1match.strip('[]')
        motif1match = motif1match.translate(None, "'")
        # m1name = str(m1nlist[index])
        moutput = open(motif1match + ".txt", "wb")
        # Looping through the second file. Also strips unnecessary text [] and '
        for index, j in enumerate(m2list):
            motif2match = str(j)
            motif2match = motif2match.strip('[]')
            motif2match = motif2match.translate(None, "'")
            m2name = str(m2nlist[index])
            m2name = m2name.strip('[]')
            m2name = m2name.translate(None, "'")	
            # Checking to see if the two match. If so, writes which two match, and increments the total number of matches found
            if motif1match in motif2match:
                moutput.write("Found match " + motif1match + " with " + motif2match + " " + m2name + "\n")
                m1m2match += 1
    # Variable for number of lines in each text file during loop
    for index, i2 in enumerate(m1list):
        motif12match = str(i2)
        motif12match = motif12match.strip('[]')
        motif12match = motif12match.translate(None, "'")
        num_lines = sum(1 for line in open(motif12match + ".txt"))
        average = num_lines/float(nummotifs)
        if average == 0.0:
            continue
        average = round(average, 4)
        avfile.write("# of binding sites for " + motif12match + " , " + str(num_lines) + "\n")

if __name__ == '__main__':
    tomatch1 = raw_input("Please enter first file to match: ")
    tomatch2 = raw_input("Please enter second file: ")
    nummots = raw_input("Please enter total number of regulatory elements: ")
    find_matches(tomatch1, tomatch2, nummots)
