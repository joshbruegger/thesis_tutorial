#!/bin/bash

# if the folder datasets/SVHN/val/labels exists, then exit
if [ -d "datasets/SVHN/val/labels" ]; then
    exit
fi

# Check if the file datasets/SVHN/train.tar.gz exists. If not, download it
if [ ! -f "datasets/SVHN/train.tar.gz" ]; then
    curl --create-dirs -o datasets/SVHN/train.tar.gz http://ufldl.stanford.edu/housenumbers/train.tar.gz
fi

# Check if the file datasets/SVHN/test.tar.gz exists. If not, download it
if [ ! -f "datasets/SVHN/test.tar.gz" ]; then
    curl --create-dirs -o datasets/SVHN/test.tar.gz http://ufldl.stanford.edu/housenumbers/test.tar.gz
fi


mkdir datasets/SVHN/train
tar -xzf datasets/SVHN/train.tar.gz -C datasets/SVHN/train
mv datasets/SVHN/train/train datasets/SVHN/train/images
python mat2yolo.py -d datasets/SVHN/train

mkdir datasets/SVHN/val
tar -xzf datasets/SVHN/test.tar.gz -C datasets/SVHN/val
mv datasets/SVHN/val/test datasets/SVHN/val/images
python mat2yolo.py -d datasets/SVHN/val