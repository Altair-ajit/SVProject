#!/bin/bash
#SBATCH -J run_get_sample_map_runner # Job name
#SBATCH --mail-user=dbraccia@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=fail # Get email for begin, end, and fail
#SBATCH --time=3-00:00:00
#SBATCH --qos=large
#SBATCH --mem=128gb

# fastq_input.txt was made using make_fastq_input_file.py
file=`cat fastq_input.txt`

# sainity check
echo $file

# running get_sample_map over all .jsdel files
python run_get_sample_map_par.py $file #and parameters from a file
