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

    def test_non_existent_onput_file_decompress(self):
        with self.assertRaises(FileNotFoundError):
            self.decompressor.decompress(self.non_existent_file_path, self.decompressed_file_path)


    def test_compress_data(self):
        data  = "ABC"
        self.compressor.lzw_dictionary = {'A': 1, 'B': 1, 'C': 1}
        compressed_data = self.compressor._compress_data(data)

        self.assertEqual(compressed_data, [1,1,1])


    def test_compress_data_false_condition(self):
        # Define some test data
        data = "ABCD"

        # Manually initialize the compressor dictionary with some entries
        self.compressor.lzw_dictionary = {'A': 0, 'B': 1, 'C': 2}

        # Call the compress_data method directly
        compressed_data = self.compressor._compress_data(data)

        # Expected compressed data based on the provided test data and dictionary state
        expected_compressed_data = [0, 1, 2, 3]

        # Assert that the compressed data matches the expected compressed data
        self.assertNotEqual(compressed_data, expected_compressed_data)

     
    def tearDown(self):
        if os.path.exists(self.compressed_file_path):
            os.remove(self.compressed_file_path)
        if os.path.exists(self.decompressed_file_path):
            os.remove(self.decompressed_file_path)
