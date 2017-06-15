# Updated 2017-06-15
# Don't recommend using this. This queried the solgenomics website directly, identified which chromosome you were looking for, and extracted the sequence you needed.
# This causes unnecessary strain on the host web server, and is also highly inefficient at gathering that data. 
# Made new script in 2014 to extract these sequences from the entire genome file, recommend using that, genome.py.

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Test feature, see if we can pull the sequence from the site
#url = raw_input("Enter a sequence to extract from solgenomics: " + acc
# Test feature, see if we can pull the sequence from the site
url = raw_input("Enter a sequence to extract from solgenomics: ")
# Create response object for the solgenomics website, then concatenate the accession number onto the search
#r  = requests.get("http://solgenomics.net/search/unigene.pl?unigene_id=" +url)
r  = requests.get("http://solgenomics.net/search/quick?term=" + url + "&x=0&y=0")
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

upstream = soup2.findAll("href")
print upstream

# Figured out the sequence is always at the first font tag, get that value into a string, then remove all tags with .text
#seq = soup2.findAll("input")
#for i in seq:
#	seqq = str(i.get('name'))	
#	if seqq == "seq":
#		seql = str(i.get('value'))
#		if 'AHRD' in seql:
#			continue
#		else:
#			result = str(i.get('value')) + "\n"
#			break
#return result
