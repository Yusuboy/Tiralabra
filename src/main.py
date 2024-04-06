from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor
from HuffmanCoding.compress import HuffmanCompress

CHOSEN_FILE = "src/example.txt"
OUTPUT_FILE_HUFFMAN = "src/compressed_W_Huff_example.bin"
OUTPUT_FILE_LZW = "src/compressed_W_LZW_example.bin"
DECOMPRESSED_FILE_HUFFMAN = "src/decompressed_W_Huff.txt"
DECOMPRESSED_FILE_LZW = "src/decompressed_W_LZW.txt"

def compress_with_huffman(input_file, output_file):
    Huffman = HuffmanCompress()
    Huffman.compress(input_file, output_file)

def decompress_with_huffman(input_file, output_file):
    Huffman = HuffmanCompress()
    Huffman.decompress(input_file, output_file)

def compress_with_lzw(input_file, output_file):
    compressor = LZWCompressor()
    compressor.compress(input_file, output_file)

def decompress_with_lzw(input_file, output_file):
    decompressor = LZWDecompressor()
    decompressor.decompress(input_file, output_file)

def main():
    while True:
        print("1. Compress with Huffman")
        print("2. Decompress with Huffman")
        print("3. Compress with LZW")
        print("4. Decompress with LZW")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            compress_with_huffman(CHOSEN_FILE, OUTPUT_FILE_HUFFMAN)
            print("File compressed with Huffman.")
        elif choice == "2":
            decompress_with_huffman(OUTPUT_FILE_HUFFMAN, DECOMPRESSED_FILE_HUFFMAN)
            print("File decompressed with Huffman.")
        elif choice == "3":
            compress_with_lzw(CHOSEN_FILE, OUTPUT_FILE_LZW)
            print("File compressed with LZW.")
        elif choice == "4":
            decompress_with_lzw(OUTPUT_FILE_LZW, DECOMPRESSED_FILE_LZW)
            print("File decompressed with LZW.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
