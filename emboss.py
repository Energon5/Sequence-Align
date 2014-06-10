from Bio.Emboss.Applications import NeedleCommandline
aseq = "alpha.faa"
bseq = "beta.faa"
needle_cline = NeedleCommandline(asequence=aseq, bsequence=bseq, gapopen = 10, gapextend = 0.5, outfile = "needle.txt")
stdout, stderr = needle_cline()

