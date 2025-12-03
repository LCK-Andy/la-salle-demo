import os

def create_100mb_file(filename="101mb_file.bin"):
    """Creates a 100MB file filled with random data."""
    size_in_mb = 101
    size_in_bytes = size_in_mb * 1024 * 1024  # Convert MB to bytes

    with open(filename, "wb") as f:
        f.write(os.urandom(size_in_bytes))
    print(f"{filename} created with size {size_in_mb}MB.")

if __name__ == "__main__":
    create_100mb_file()