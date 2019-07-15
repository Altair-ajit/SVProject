#!/bin/bash
#SBATCH -J run_ICRA_runner # Job name
#SBATCH --mail-user=dbraccia@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=fail # Get email for begin, end, and fail
#SBATCH --time=3-00:00:00
#SBATCH --qos=large
#SBATCH --mem=128gb
#SBATCH --array=1-20

# fastq_input.txt was made using make_fastq_input_file.py
file=`head -n ${SLURM_ARRAY_TASK_ID} fastq_input.txt | tail -n 1`

# checking progress of job
echo $file

# running ICRA over current sample
python run_ICRA_par.py $file #and parameters from a file
