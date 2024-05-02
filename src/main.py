import os
import time
from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor
from HuffmanCoding.huffman_coding import HuffmanCompress
from file_utils import is_txt_file, get_file_size, delete_files_in_folder
from ui import display_file_lists, display_compression_stats, display_decompression_stats

from prettytable import PrettyTable


TEXT_FILE_FOLDER = "src/textfiles"
BINARY_FILE_FOLDER = "src/BinFiles"
DECOMPRESSED_FILE_FOLDER = "src/decompressedFiles"
CLEAN_FOLDERS = ["src/BinFiles", "src/decompressedFiles"]


def compress_with_lzw(input_file, output_file):
    compressor = LZWCompressor()
    compressor.compress(input_file, output_file)

def decompress_with_lzw(input_file, output_file):
    decompressor = LZWDecompressor()
    decompressor.decompress(input_file, output_file)

def compare_compression(filename):
    input_file = os.path.join(TEXT_FILE_FOLDER, filename)
    huffman_output_file = os.path.join(BINARY_FILE_FOLDER, f"{os.path.splitext(filename)[0]}_Huffman.bin")
    lzw_output_file = os.path.join(BINARY_FILE_FOLDER, f"{os.path.splitext(filename)[0]}_LZW.bin")

    # Compress with Huffman
    huffman_start_time = time.time()
    h.compress(input_file, huffman_output_file)
    huffman_end_time = time.time()
    huffman_compressed_size = get_file_size(huffman_output_file)

    # Compress with LZW
    LZW_start_time = time.time()
    compress_with_lzw(input_file, lzw_output_file)
    lzw_end_time = time.time()
    lzw_compressed_size = get_file_size(lzw_output_file)

    # Display compression statistics in a pretty table
    table = PrettyTable()
    table.field_names = ["Algorithm", "Original Size", "Compressed Size", "Compression Ratio", "Compression Time"]
    table.add_row(["Huffman", get_file_size(input_file), huffman_compressed_size, ((get_file_size(input_file) - huffman_compressed_size) / get_file_size(input_file)) * 100, huffman_end_time - huffman_start_time])
    table.add_row(["LZW", get_file_size(input_file), lzw_compressed_size, ((get_file_size(input_file) - lzw_compressed_size) / get_file_size(input_file)) * 100, lzw_end_time - LZW_start_time])
    print("Comparison of Compression Algorithms:")
    print(table)

h = HuffmanCompress()


def clean_up():
    for folder in CLEAN_FOLDERS:
        delete_files_in_folder(folder)
    

def main():
    while True:
        display_file_lists()
        print("1. Compress with Huffman")
        print("2. Decompress with Huffman")
        print("3. Compress with LZW")
        print("4. Decompress with LZW")
        print("5. Compare algorithms")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            filename = input("Enter the name of the text file to compress with Huffman: ")
            input_file = os.path.join(TEXT_FILE_FOLDER, filename)
            if not os.path.isfile(input_file):
                print("Invalid filename. Please check the filename and try again.")
                continue
            output_file = os.path.join(BINARY_FILE_FOLDER, f"{os.path.splitext(filename)[0]}_Huff.bin")
            start_time = time.time()
            h.compress(input_file, output_file)
            end_time = time.time()
            compressed_size = get_file_size(output_file)
            original_size = get_file_size(input_file)
            display_compression_stats("Huffman", original_size, compressed_size, end_time - start_time)

            # compression_ratio = ((original_size - compressed_size) / original_size) * 100

            # print(f"File compressed with Huffman.\nCompression ratio: {compression_ratio}\nCompression time: {end_time - start_time} seconds")

        elif choice == "2":
            filename = input("Enter the name of the compressed file to decompress with Huffman: ")
            check = is_txt_file(filename)
            if check == True:
                print("File must be compressed first")
            else:
                input_file = os.path.join(BINARY_FILE_FOLDER, filename)
                if not os.path.isfile(input_file):
                    print("Invalid filename. Please check the filename and try again.")
                    continue
                output_file = os.path.join(DECOMPRESSED_FILE_FOLDER, f"{os.path.splitext(filename)[0]}.txt")
                start_time = time.time()
                h.decompress(input_file, output_file)
                end_time = time.time()
                display_decompression_stats("Huffman", end_time - start_time)


        elif choice == "3":
            filename = input("Enter the name of the text file to compress with LZW: ")
            input_file = os.path.join(TEXT_FILE_FOLDER, filename)
            if not os.path.isfile(input_file):
                print("Invalid filename. Please check the filename and try again.")
                continue
            output_file = os.path.join(BINARY_FILE_FOLDER, f"{os.path.splitext(filename)[0]}_LZW.bin")
            start_time = time.time()
            compress_with_lzw(input_file, output_file)
            end_time = time.time()
            compressed_size = get_file_size(output_file)
            original_size = get_file_size(input_file)
            display_compression_stats("LZW", original_size, compressed_size, end_time - start_time)
            # compression_ratio = ((original_size - compressed_size) / original_size) * 100

            # print(f"File compressed with LZW.\nCompression ratio: {compression_ratio}\nCompression time: {end_time - start_time} seconds")

        elif choice == "4":
            filename = input("Enter the name of the compressed file to decompress with LZW: ")
            check = is_txt_file(filename)
            if check == True:
                print("File must be compressed first")
            input_file = os.path.join(BINARY_FILE_FOLDER, filename)
            if not os.path.isfile(input_file):
                print("Invalid filename. Please check the filename and try again.")
                continue
            output_file = os.path.join(DECOMPRESSED_FILE_FOLDER, f"compressed_{os.path.splitext(filename)[0]}.txt")
            start_time = time.time()
            decompress_with_lzw(input_file, output_file)
            end_time = time.time()

            display_decompression_stats("LZW", end_time - start_time)

        elif choice == "5":
            # Compare compression algorithms
            filename = input("Enter the name of the text file to compare compression algorithms: ")
            input_file = os.path.join(TEXT_FILE_FOLDER, filename)
            if not os.path.isfile(input_file):
                print("Invalid filename. Please check the filename and try again.")
                continue
            compare_compression(filename)


        elif choice == "6":
            clean_up()
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
