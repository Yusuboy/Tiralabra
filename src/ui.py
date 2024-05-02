from prettytable import PrettyTable
from file_utils import list_files, get_file_size
import os
import time
from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor
from HuffmanCoding.huffman_coding import HuffmanCompress

TEXT_FILE_FOLDER = "src/textfiles"
BINARY_FILE_FOLDER = "src/BinFiles"
DECOMPRESSED_FILE_FOLDER = "src/decompressedFiles"

def display_file_lists():
    text_files = list_files(TEXT_FILE_FOLDER, ".txt")
    binary_files = list_files(BINARY_FILE_FOLDER, ".bin")

    if not text_files and not binary_files:
        print("No files found in the folders.")
    else:
        max_files = max(len(text_files), len(binary_files))

        table = PrettyTable()
        table.field_names = ["Available Text Files", "Available Binary Files"]

        for i in range(max_files):
            text_file = text_files[i] if i < len(text_files) else ""
            binary_file = binary_files[i] if i < len(binary_files) else ""
            table.add_row([text_file, binary_file])
        print(table)


def display_compression_stats(algorithm, original_size, compressed_size, compression_time):
    table = PrettyTable()
    table.field_names = ["Algorithm", "Original Size", "Compressed Size", "Compression Ratio", "Compression Time"]
    table.add_row([algorithm, original_size, compressed_size, ((original_size - compressed_size) / original_size) * 100, compression_time])
    print()
    print("Compression Statistics:")
    print(table)


def display_decompression_stats(algorithm, decompression_time):
    table = PrettyTable()
    table.field_names = ["Algorithm", "deompression Time"]
    table.add_row([algorithm, decompression_time])
    print("Decompression Statistics:")
    print(table)