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

# Figured out the sequence is always at the first font tag (Possibility this might only work with old accession numbers), get that value into a string, then remove all tags with .text
seq = soup.find("font")
cleanseq = seq.text

aseq = cleanseq
bseq = cleanseq
needle_cline = NeedleCommandline(asequence=aseq, bsequence=bseq, gapopen = 10, gapextend = 0.5, outfile = "needle.txt")
stdout, stderr = needle_cline()

