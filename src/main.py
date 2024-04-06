from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor

from HuffmanCoding.compress import HuffmanCompress


CHOSEN_FILE = "src/example.txt"

OUTPUT_FILE = "src/compressed_W_Huff_example.bin"
OUTPUT_FILE2 = "src/compressed_W_LZW_example.bin"


DECOMPRESSED_FILE = "src/decompressed_W_Huff.txt"
DECOMPRESSED_FILE2 = "src/decompressed_W_LZW.txt"






Huffman = HuffmanCompress()

Huffman.compress(CHOSEN_FILE, OUTPUT_FILE)
Huffman.decompress(OUTPUT_FILE, DECOMPRESSED_FILE)

compressor = LZWCompressor()
decompressor = LZWDecompressor()

compressor.compress(CHOSEN_FILE, OUTPUT_FILE2)
decompressor.decompress(OUTPUT_FILE2, DECOMPRESSED_FILE2)