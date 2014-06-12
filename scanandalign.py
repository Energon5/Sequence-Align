from bs4 import BeautifulSoup
import requests
import pandas as pd
from Bio.Emboss.Applications import NeedleCommandline

def genscan(acc):
	
	# Test feature, see if we can pull the sequence from the site
	#url = raw_input("Enter a sequence to extract from solgenomics: " + acc
	while True:
		if acc == "nan":
			break
		elif acc == "none":
			break
		elif acc == "None":
			break
		# Create response object for the solgenomics website, then concatenate the accession number onto the search
		r  = requests.get("http://solgenomics.net/search/unigene.pl?unigene_id=" + acc)

		# Assign the site text 
		data = r.text

		# bs4 object + getting the text
		soup = BeautifulSoup(data)
		soup.get_text()

		# Figured out the sequence is always at the first font tag, get that value into a string, then remove all tags with .text
		seq = soup.find("font")
		cleanseq = seq.text

		#This if checks to see if the value contains a sequence or not. If it doesn't, then it looks in the next available spot. The else just prints if sequence is present
		if seq.text == 'none':
			seq = soup.findChildren("font")
			cleanseq = seq[1].text
			return cleanseq
		return cleanseq


io = pd.read_csv('gongcsv.csv', sep=",", usecols=(0,))
iolist = map(list, io.values)

genenames = pd.read_csv('gongcsv.csv', sep=",", usecols=(1,))
namelist = map(list, genenames.values)


seqb = iolist[0]
seqbs = str(seqb).strip('[]')
seqaname = namelist[0]
seqanamest = str(seqaname).strip('[]')
seqbs = seqbs.translate(None, "'")
seqa = genscan(seqbs)
seqbase = open("seq1.fasta", "w")
seqbase.write(">" + seqbs + seqanamest)
seqbase.write(seqa)
seqbase.close()

seqcompare = open("seq2.fasta", "wb")
for nums in iolist:
	if nums == "nan":
		continue
	seq2bs = str(nums)
	seq2bsa = seq2bs.strip('[]')
	seq2bsa = seq2bsa.translate(None, "'")
	seqcompare.write(">" + seq2bsa)
	seqb = genscan(seq2bsa)
	seqcompare.write(str(seqb))
	seqcompare.write('\n')
seqcompare.close()

needle_cline = NeedleCommandline(asequence="seq1.fasta", bsequence="seq2.fasta", gapopen = 10, gapextend = 0.5, outfile = "needle.txt")
stdout, stderr = needle_cline()

