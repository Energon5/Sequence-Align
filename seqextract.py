from bs4 import BeautifulSoup
import requests
from Bio.Emboss.Applications import NeedleCommandline

# Test feature, see if we can pull the sequence from the site
url = raw_input("Enter a sequence to extract from solgenomics: ")

# Create response object for the solgenomics website, then concatenate the accession number onto the search
r  = requests.get("http://solgenomics.net/search/unigene.pl?unigene_id=" +url)

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
	print cleanseq
else:
	print cleanseq





