import unittest
from LZW.compress import LZWCompressor
from LZW.decompress import LZWDecompressor
import os

class TestLZW(unittest.TestCase):
    def setUp(self):
        self.input_file_path = "src/tests/test.txt"
        self.compressed_file_path = "src/tests/compressed_test.bin"
        self.decompressed_file_path = "src/tests/decompressed_test_file.txt"
        self.non_existent_file_path = "src/tests/non_existent_file.txt" 
        self.compressor = LZWCompressor()
        self.decompressor = LZWDecompressor()

    def test_compress_decompress(self):
        self.compressor.compress(self.input_file_path, self.compressed_file_path)
        self.decompressor.decompress(self.compressed_file_path, self.decompressed_file_path)

        with open(self.input_file_path, 'r') as inptut_file:
            original_data = inptut_file.read()

        with open(self.decompressed_file_path, 'r') as decompressed_file:
            decompressed_data = decompressed_file.read()

        self.assertEqual(original_data,decompressed_data)

    def test_non_existent_input_file_compress(self):
        with self.assertRaises(FileNotFoundError):
            self.compressor.compress(self.non_existent_file_path, self.compressed_file_path)

    def test_non_existent_input_file_decompress(self):
        with self.assertRaises(FileNotFoundError):
            self.decompressor.decompress(self.non_existent_file_path, self.decompressed_file_path)

     
    def tearDown(self):
        if os.path.exists(self.compressed_file_path):
            os.remove(self.compressed_file_path)
        if os.path.exists(self.decompressed_file_path):
            os.remove(self.decompressed_file_path)
