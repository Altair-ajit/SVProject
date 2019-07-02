#!/bin/bash
#SBATCH -J run_get_sample_map_runner # Job name
#SBATCH --mail-user=dbraccia@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=fail # Get email for begin, end, and fail
#SBATCH --time=3-00:00:00
#SBATCH --qos=large
#SBATCH --mem=128gb

#test
echo hi

# running work_on_collection for get_sample_map output dictionary
python run_work_on_collection_par.py $1
