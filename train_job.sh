#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpus-per-node=a100:1
#SBATCH --tasks-per-node=6
#SBATCH --job-name=jupyter
#SBATCH --mem=16G
#SBATCH --partition=gpu
#SBATCH --time=04:00:00

# Clear the module environment
module purge
# Load the Python version that has been used to construct the virtual environment
module load PyTorch/1.12.1-foss-2022a-CUDA-11.7.0

# Activate the virtual environment
source ~/thesis/env/bin/activate

python3 ~/thesis/thesisTutorial/train.py

deactivate