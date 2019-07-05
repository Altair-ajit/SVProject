#!/bin/bash
#SBATCH -J batch_download # Job name
#SBATCH --mail-user=dbraccia@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=fail # Get email for begin, end, and fail
#SBATCH --time=0-18:00:00
#SBATCH --qos=throughput
#SBATCH --mem=36gb
#SBATCH --array=1-1523

# fastq_links.txt was made using make_fastq_links_file.py
file=`head -n ${SLURM_ARRAY_TASK_ID} fastq_links.txt | tail -n 1`

# feed current line of fasq_links.txt to wget after seperating at the ';' for paired end
new_file=`echo $file | tr ';' ' '`
echo $new_file
wget -P ./PRJEB11532/ $new_file
