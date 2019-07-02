print 'starting work_on_collection script'
from SGVFinder import work_on_collection
import numpy as np
import sys
from os.path import join

# initializing
print 'getting sample map dictionary from standard input'
OUTPUT_FOLDER = '../results/subset_example/'
sample_map_dict = sys.argv[1]
print sample_map_dict

# importing samp_to_map dictionary
samp_to_map = np.load(join(OUTPUT_FOLDER, sample_map_dict)).item()

print 'running work_on_collection'
vsgv, dsgv = work_on_collection(samp_to_map, 10, 0.25, 0.95, 0.25, 0.125, 0.02,
                                0.95, 'betaprime', 0.01, 10, 85, join(OUTPUT_FOLDER, 'browser'))
vsgv.to_pickle(join(OUTPUT_FOLDER, 'vsgv.df'))
dsgv.to_pickle(join(OUTPUT_FOLDER, 'dsgv.df'))
