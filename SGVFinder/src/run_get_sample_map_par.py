#===============================================================================
# this script executes the first step of SGVFinder: `get_sample_map()``
# get_sample_map() creates a dictionary whos keys are the sample IDs and
# whos values are the outputs of ICRA (the .jsdel files).
# NOTE: at this point, the code below is not parallelized, as it would be difficult
#       to take advantage of the cluster's distribution abilites
#===============================================================================
print 'starting script'
from SGVFinder import get_sample_map
import numpy as np
import sys

# getting all sample names into list
print 'getting sample names from std. input'
samples = sys.argv[1:len(sys.argv)]
OUTPUT_FOLDER = '../results/subset_example/'

# sainity check
print samples

print 'writing samp_to_map'
samp_to_map = {s: get_sample_map(OUTPUT_FOLDER + s + '.jsdel', .01, 100, 10) \
               for s in samples}
np.save(join(OUTPUT_FOLDER, 'subset_dict.npy'), samp_to_map)
