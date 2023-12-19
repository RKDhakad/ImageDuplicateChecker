import os
import sys
import hashlib
import shutil

def generate_hash(image_path):
    """Generate a hash for the given image file."""
    hasher = hashlib.md5()
    with open(image_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# hasher = hashlib.md5(): This line creates an MD5 hash object using the hashlib module. MD5 is a widely used cryptographic hash function.
# with open(image_path, 'rb') as f:: This line opens the image file in binary mode ('rb'), allowing the function to read the file as bytes. The with statement ensures that the file is properly closed after reading.
# while chunk := f.read(8192):: This line reads the file in chunks of 8192 bytes (8KB). The walrus operator (:=) is used to assign the result of f.read(8192) to the variable chunk and also check if the result is not an empty byte string (indicating the end of the file).
# hasher.update(chunk): Inside the loop, each chunk of the file is passed to the update method of the hash object. This updates the hash with the content of the current chunk.
# return hasher.hexdigest(): After reading the entire file and updating the hash, the function returns the hexadecimal representation of the digest using the hexdigest method. The resulting hash is a fixed-size string, typically 32 characters for MD5.
# In summary, this function reads an image file in chunks, updates an MD5 hash object with each chunk, and finally returns the hexadecimal representation of the MD5 hash for the entire file. This hash can be used as a unique identifier for the content of the image file.

def check_duplicate(hash_pool, new_hash):
    """Check if the new hash is present in the hash pool."""
    return new_hash in hash_pool

def update_hash_pool(hash_pool, new_hash):
    """Update the hash pool with the new hash."""
    hash_pool.add(new_hash)

def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def copy_to_images_directory(new_image_path, images_directory):
    """Copy the new image to the 'images' directory."""
    filename = os.path.basename(new_image_path)
    destination_path = os.path.join(images_directory, filename)
    shutil.copyfile(new_image_path, destination_path)
    print(f"Image copied to {destination_path}")

def main():
    # Step 1: Create or load hash pool
    hash_pool_file = 'hash_pool.txt'
    if os.path.exists(hash_pool_file):
        with open(hash_pool_file, 'r') as f:
            hash_pool = set(f.read().splitlines())
    else:
        hash_pool = set()

    # Step 2: Create or check the 'images' directory
    images_directory = 'images'
    create_directory(images_directory)

    # Step 3: Check and return message for duplicate/similar images
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_new_image>")
        sys.exit(1)

    new_image_path = sys.argv[1]
    if not os.path.exists(new_image_path):
        print(f"Error: Image not found at {new_image_path}")
        sys.exit(1)

    new_hash = generate_hash(new_image_path)

    if check_duplicate(hash_pool, new_hash):
        print("Duplicate image! Do not process.")
    else:
        print("New image. Processing...")
        copy_to_images_directory(new_image_path, images_directory)

        # Step 4: Update hash pool with new image
        update_hash_pool(hash_pool, new_hash)
        with open(hash_pool_file, 'w') as f:
            f.write('\n'.join(hash_pool))

if __name__ == "__main__":
    main()
