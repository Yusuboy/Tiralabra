from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor

CHOSEN_FILE = "src/example.txt"
OUTPUT_FILE = "src/compressed_example.bin"

compressor = LZWCompressor()
decompressor = LZWDecompressor()
compressor.compress(CHOSEN_FILE, OUTPUT_FILE)

DECOMPRESSED_FILE = "src/decompressed.txt"

decompressor.decompress(OUTPUT_FILE, DECOMPRESSED_FILE)
