import os
import time
from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor
from HuffmanCoding.compress import HuffmanCompress

CHOSEN_FILE = "src/example.txt"
OUTPUT_FILE_HUFFMAN = "src/compressed_W_Huff_example.bin"
OUTPUT_FILE_LZW = "src/compressed_W_LZW_example.bin"
DECOMPRESSED_FILE_HUFFMAN = "src/decompressed_W_Huff.txt"
DECOMPRESSED_FILE_LZW = "src/decompressed_W_LZW.txt"


def get_file_size(file_path):
    return os.path.getsize(file_path)

def compress_with_lzw(input_file, output_file):
    compressor = LZWCompressor()
    compressor.compress(input_file, output_file)

def decompress_with_lzw(input_file, output_file):
    decompressor = LZWDecompressor()
    decompressor.decompress(input_file, output_file)

h = HuffmanCompress()

def main():
    while True:
        print("1. Compress with Huffman")
        print("2. Decompress with Huffman")
        print("3. Compress with LZW")
        print("4. Decompress with LZW")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            start_time = time.time()
            h.compress(CHOSEN_FILE, OUTPUT_FILE_HUFFMAN)
            end_time = time.time()
            compressed_size = get_file_size(OUTPUT_FILE_HUFFMAN)
            original_size = get_file_size(CHOSEN_FILE)
            compression_ratio = ((original_size - compressed_size) / original_size) * 100

            print(f"File compressed with Huffman.\nCompression ratio: {compression_ratio}\nCompression time: {end_time - start_time} seconds")
        elif choice == "2":
            start_time = time.time()
            h.decompress(OUTPUT_FILE_HUFFMAN, DECOMPRESSED_FILE_HUFFMAN)
            end_time = time.time()
            print(f"File decompressed with Huffman.\nCompression time: {end_time - start_time} seconds")
        elif choice == "3":
            start_time = time.time()
            compress_with_lzw(CHOSEN_FILE, OUTPUT_FILE_LZW)
            end_time = time.time()
            compressed_size = get_file_size(OUTPUT_FILE_LZW)
            original_size = get_file_size(CHOSEN_FILE)
            compression_ratio = ((original_size - compressed_size) / original_size) * 100
            print(f"File compressed with LZW.\nCompression ratio: {compression_ratio}\nCompression time: {end_time - start_time} seconds")
        elif choice == "4":
            start_time = time.time()
            decompress_with_lzw(OUTPUT_FILE_LZW, DECOMPRESSED_FILE_LZW)
            end_time = time.time()
            print(f"File decompressed with Huffman.\nCompression time: {end_time - start_time} seconds")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
