# ImageDuplicateChecker
# Image Duplicate Checker

## Overview

This Python script checks whether a new image is a duplicate or similar to existing images by generating and comparing image hashes. If the image is determined to be new, it is then copied to the 'images' directory.

## Author

- **Author:** Ravi Dhakad

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/RKDhakad/ImageDuplicateChecker.git
   cd image-duplicate-checker
   python main.py <path_to_new_image>

Replace <path_to_new_image> with the actual path to the new image you want to check.

## Functionality
- Hash Generation:
   The script generates an MD5 hash for each image file.
   The hash is used as a unique identifier for the content of the image.

- Duplicate Check:
   The script checks whether the generated hash of the new image matches any existing hashes stored in the hash pool.

- Directory Handling:
   The 'images' directory is created if it doesn't exist.

-Copy to 'images' Directory:
   If the image is determined to be new, it is copied to the 'images' directory for further processing.

-Hash Pool Update:
   The script updates the hash pool with the new image hash and stores it in the 'hash_pool.txt' file.
