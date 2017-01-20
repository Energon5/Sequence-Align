from bs4 import BeautifulSoup
import requests
import pandas as pd
from Bio.Emboss.Applications import NeedleCommandline

def genscan(acc):
	
	# Test feature, see if we can pull the sequence from the site
	#url = raw_input("Enter a sequence to extract from solgenomics: " + acc

	# Test feature, see if we can pull the sequence from the site
	#url = raw_input("Enter a sequence to extract from solgenomics: ")

	# Create response object for the solgenomics website, then concatenate the accession number onto the search
	#r  = requests.get("http://solgenomics.net/search/unigene.pl?unigene_id=" +url)

	r  = requests.get("http://solgenomics.net/search/quick?term=" + acc + "&x=0&y=0")

	# Assign the site text 
	data = r.text

	# bs4 object + getting the text
	soup = BeautifulSoup(data)
	soup.get_text()

	link = soup.findAll("a")
	links = ""
	for l in link:
		li = str(l.get('href'))
		if '/feature/1' in li:
			links = str(l.get('href'))
			break
	r2 = requests.get("http://solgenomics.net/" + links)

	mdata = r2.text
	soup2 = BeautifulSoup(mdata)
	soup2.get_text()

	# Figured out the sequence is always at the first font tag, get that value into a string, then remove all tags with .text
	seq = soup2.findAll("input")
	for i in seq:
		seqq = str(i.get('name'))	
		if seqq == "seq":
			seql = str(i.get('value'))
			if 'AHRD' in seql:
				continue
			else:
				result = str(i.get('value')) + "\n"
				break
	return result

file1 = raw_input("Please enter name desired for first sequence file: ")
file2 = raw_input("Please enter name desired for second sequencefile: ")
csvname = raw_input("Please enter name of csv file to pull sequences from: ")
genenames = pd.read_csv(csvname + '.csv', sep=",", usecols=(1,))
namelist = map(list, genenames.values)

seqb = namelist[0]
seqbs = str(seqb).strip('[]')
seqbs = seqbs.translate(None, "'")
seqa = genscan(seqbs)
seqbase = open(file1 + ".fasta", "w")
seqbase.write(seqa)
seqbase.close()

seqcompare = open(file2 + ".fasta", "wb")
for nums in namelist:
	if nums == "nan":
		continue
	seq2bs = str(nums)
	seq2bsa = seq2bs.strip('[]')
	seq2bsa = seq2bsa.translate(None, "'")
	seqb = genscan(seq2bsa)
	seqcompare.write(str(seqb))
seqcompare.close()

#needle_cline = NeedleCommandline(asequence="seq1.fasta", bsequence="seq2.fasta", gapopen = 10, gapextend = 0.5, outfile = "needle.txt")
#stdout, stderr = needle_cline()

