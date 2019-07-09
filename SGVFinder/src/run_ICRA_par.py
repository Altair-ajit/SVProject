#==============================================================================
# NOTE: This is an attempt to parallelize the subset_example.py script
# This file provides is an adaptation of linear_example.py which just runs ICRA
# on a single sample. The idea is to run this script through a shell script 
# which uses the cluster to run it over all samples through the .sh file named 
# "run_ICRA_runner.sh"
# NOTE 2: See the README.md for requirements etc.
#==============================================================================
from os.path import join, splitext, basename, exists
from ICRA import single_file
from SGVFinder import get_sample_map, work_on_collection
import os
import sys
import time
t_start = time.time()
INPUT_FOLDER = '../data/PRJEB11532_subset/'
OUTPUT_FOLDER = '../results/subset_example_timed/'
if not os.path.exists(join(OUTPUT_FOLDER, 'browser')):
    os.mkdir(join(OUTPUT_FOLDER, 'browser'))

# =============================================================================

print 'initialization done ... running single_file()'
# for paired-end experiments
f = sys.argv[1]
if os.path.exists(join(INPUT_FOLDER, f + '_1.fastq')):
    fq_1 = join(INPUT_FOLDER, f + '_1.fastq')
    print fq_1
    fq_2 = join(INPUT_FOLDER, f + '_2.fastq')
    print fq_2
    t_index, t_GEM, t_init, t_iter, _ = single_file(fq_1, fq_2, OUTPUT_FOLDER, 8, True, 1e-6, 100, 10, 100, 100, 60, 1e5, 2e7, 'genomes', False)
else: # for single-end experiments
    fq = join(INPUT_FOLDER, f + '.fastq')
    print fq
    t_index, t_GEM, t_init, t_iter, _ = single_file(fq, None, OUTPUT_FOLDER, 8, True, 1e-6, 100, 10, 100, 100, 60, 1e5, 2e7, 'genomes', False)

print '\nAll time stamps below are in minutes\n'
print 'time taken to index reads', round(t_index / 60)
print 'time taken to run GEM Mapper', round(t_GEM / 60)
print 'time taken to initialize read parameters', round(t_init / 60)
print 'time taken to run iterative read assignment', round(t_iter / 60)
print '\ntime taken to run whole sample', round((time.time() - t_start) / 60)
# =============================================================================
