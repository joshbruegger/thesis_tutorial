#!/bin/bash
#SBATCH --job-name=trainYOLO_Bruegger
#SBATCH --output=job-%j.log
#SBATCH --nodes=1
#SBATCH --gpus-per-node=a100:1
#SBATCH --mem=16G
#SBATCH --partition=gpu
#SBATCH --time=01:00:00

# Clear the module environment
module purge
# Load the Python version that has been used to construct the virtual environment
module load PyTorch/1.12.1-foss-2022a-CUDA-11.7.0

# Activate the virtual environment
source ~/thesis/env/bin/activate

# Change directory to local directory
cd $TMPDIR

# Copy the repository to the local directory
git clone https://github.com/joshbruegger/thesis_tutorial

# Change directory to the repository
cd thesis_tutorial

# if the database folder does not exist, run the setup.sh script
if [ ! -d "database" ]; then
    bash setup.sh
fi

# Run the training script
python3 ./train.py

# copy the run directory to scratch
cp -r runs /scratch/$USER/results/

deactivate