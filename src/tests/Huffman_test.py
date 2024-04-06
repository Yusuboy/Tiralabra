import unittest
from HuffmanCoding.compress import HuffmanCompress

import os

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.input_file_path = "src/tests/test.txt"
        self.compressed_file_path = "src/tests/compressed_test.bin"
        self.decompressed_file_path = "src/tests/decompressed_test_file.txt"
        self.Huffman = HuffmanCompress()

    def test_compress_decompress(self):
        self.Huffman.compress(self.input_file_path, self.compressed_file_path)
        self.Huffman.decompress(self.compressed_file_path, self.decompressed_file_path)

        with open(self.input_file_path, 'r') as inptut_file:
            original_data = inptut_file.read()

        with open(self.decompressed_file_path, 'r') as decompressed_file:
            decompressed_data = decompressed_file.read()

        self.assertEqual(original_data,decompressed_data)

    def test_heapnode_equality(self):
        node1 = HuffmanCompress.HeapNode('a', 5)
        node2 = HuffmanCompress.HeapNode('b', 5)
        node3 = HuffmanCompress.HeapNode('c', 7)

        self.assertTrue(node1 == node2)
        self.assertFalse(node1 == node3)



    def tearDown(self):
        if os.path.exists(self.compressed_file_path):
            os.remove(self.compressed_file_path)
        if os.path.exists(self.decompressed_file_path):
            os.remove(self.decompressed_file_path)