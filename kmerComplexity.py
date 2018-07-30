__author__="Adam Healey, ahealey@hudsonalpha.org"
__date__ ="Created:  8/18/16"

from sys import stdin, stdout, argv
from optparse import OptionParser

#==============================================================
#read in a kmer
#print the sequence
#print the length of the kmer
#calculate complexity
#return is complexity is high enough

usage = "usage: %prog [complexity number]"
parser = OptionParser(usage)
(options, args) = parser.parse_args()

if ( len(args) !=1 ):
    parser.error ("Incorrect number of arguments. Provide a number and kmers with > # of nucleotides than number will be returned")
    ####



Script, Counter = argv
Counter = float(argv[1])

def real_main():
    for line in stdin:
        kmer = line.strip()
        length = float(len(kmer))
        A_count = float(kmer.count("A"))
        C_count = float(kmer.count("C"))
        G_count = float(kmer.count("G"))
        T_count = float(kmer.count("T"))

        if (A_count > Counter) and (C_count > Counter) and (G_count > Counter) and (T_count > Counter):
            print "%s\t%d\t%d\t%d\t%d\t%d" % (kmer, length, A_count, C_count, T_count, G_count) 
            ####



#==============================================================
if ( __name__ == '__main__' ):
    real_main()


