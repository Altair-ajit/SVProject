# NOTE: This script requires that .fastq sequence files are already downloaded
# to the ../data/PRJEB11532/ directory. This is just the accession number to
# the samples for the Israeli cohort. In principle, this folder could contain
# samples from any WGS study.
import os

experiments = os.listdir('../data/Israeli_cohort/')

out = [i[0:10] for i in experiments]
out_sorted = sorted(set(out))

with open('fastq_input.txt', 'w') as f:
    for item in out_sorted:
        print >> f, item
