from LZW.compress import LZWCompressor

CHOSEN_FILE = "src/example.txt"
OUTPUT_FILE = "src/compressed_example.bin"

compressor = LZWCompressor()
compressor.compress(CHOSEN_FILE, OUTPUT_FILE)
