import unittest
from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor

class TestLZW(unittest.TestCase):
    def setUp(self):
        self.compressor = LZWCompressor()
        self.decompressor = LZWDecompressor()

    def Test_compress_decompress(self):
        input_file_path = "src/tests/test_file.txt"
        compressed_file_path = "src/tests/compressed_test_file.txt"
        decompressef_file_path = "src/tests/decompressed_test_file.txt"

        self.compressor.compress(input_file_path,compressed_file_path)
        self.decompressor.decompress(compressed_file_path,decompressef_file_path)

        with open(input_file_path, 'r') as inptut_file:
            original_data = inptut_file.read()

        with open(decompressef_file_path, 'r') as decompressed_file:
            decompressed_data = decompressed_file.read()

        self.assertEqual(original_data,decompressed_data)