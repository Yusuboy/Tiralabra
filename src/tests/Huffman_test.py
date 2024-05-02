import unittest
from HuffmanCoding.huffman_coding import HuffmanCompress

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


    def test_heap_build(self):
        frequency = {'a':5, 'b':4, 'c':9}
        self.Huffman.build_heap(frequency)
        heap_nodes = []
        for node in self.Huffman.heap:
            heap_nodes.append(node.freq)
        
        self.assertEqual(heap_nodes, [4,5,9])

    
    def test_merge_nodes(self):
        frequency = {'a':5, 'b':4, 'c':9}
        self.Huffman.build_heap(frequency)
        self.Huffman.merge_nodes()

        self.assertEqual(len(self.Huffman.heap), 1)

    
    def test_encoded_text(self):
        input_string = "helloworld"

        frequency = {'h':1,'e':1,'l':3, 'o':2, 'w':1, 'r':1, 'd':1}

        self.Huffman.build_heap(frequency)
        self.Huffman.merge_nodes()
        self.Huffman.make_nodes()

        encoded_text = self.Huffman.encode_text(input_string)

        self.assertEqual(encoded_text,"101000111110110001101111000")



    def tearDown(self):
        if os.path.exists(self.compressed_file_path):
            os.remove(self.compressed_file_path)
        if os.path.exists(self.decompressed_file_path):
            os.remove(self.decompressed_file_path)