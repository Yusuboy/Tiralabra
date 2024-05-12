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


    def test_frequency_dictionary(self):

        # Test with empty string
        text_empty = ""
        self.assertEqual(self.Huffman.frequency_dictionary(text_empty), {})

        # Test with single character
        text_single_char = "a"
        self.assertEqual(self.Huffman.frequency_dictionary(text_single_char), {'a': 1})

        # Test with multiple characters
        text_multiple_chars = "aabbbccc"
        expected_freq = {'a': 2, 'b': 3, 'c': 3}
        self.assertEqual(self.Huffman.frequency_dictionary(text_multiple_chars), expected_freq)

        # Test with special characters and whitespace
        text_special_chars = "!@#$%^&*()_+ 12345"
        expected_freq_special = {'!': 1, '@': 1, '#': 1, '$': 1, '%': 1, '^': 1, '&': 1, '*': 1, '(': 1, ')': 1, '_': 1, '+': 1, ' ': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1}
        self.assertEqual(self.Huffman.frequency_dictionary(text_special_chars), expected_freq_special)

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

    def test_make_nodes_helper(self):
        root = self.Huffman.HeapNode(None, 5)
        root.left = self.Huffman.HeapNode('a', 2)
        root.right = self.Huffman.HeapNode(None, 3)
        root.right.left = self.Huffman.HeapNode('b', 1)
        root.right.right = self.Huffman.HeapNode('c', 2)

        expected_nodes = {'a': '0', 'b': '10', 'c': '11'}
        expected_reverse_mapping = {'0': 'a', '10': 'b', '11': 'c'}

        self.Huffman.make_nodes_helper(root, "")
        self.assertEqual(self.Huffman.nodes, expected_nodes)
        self.assertEqual(self.Huffman.reverse_mapping, expected_reverse_mapping)

    
    def test_encoded_text(self):
        input_string = "helloworld"

        frequency = {'h':1,'e':1,'l':3, 'o':2, 'w':1, 'r':1, 'd':1}

        self.Huffman.build_heap(frequency)
        self.Huffman.merge_nodes()
        self.Huffman.make_nodes()

        encoded_text = self.Huffman.encode_text(input_string)

        self.assertEqual(encoded_text,"101000111110110001101111000")


    def test_pad_encoded_sequence(self):
        # Test with an empty string
        encoded_text_empty = ""
        expected_padded_empty = "0000100000000000"
        self.assertEqual(self.Huffman.pad_encoded_sequence(encoded_text_empty), expected_padded_empty)

        # sequence length of 7
        encoded_text_len_7 = "1010101"
        expected_padded_len_7 = "0000000110101010"
        self.assertEqual(self.Huffman.pad_encoded_sequence(encoded_text_len_7), expected_padded_len_7)

        # sequence length of 8
        encoded_text_len_8 = "10101010"
        expected_padded_len_8 = "000010001010101000000000"
        self.assertEqual(self.Huffman.pad_encoded_sequence(encoded_text_len_8), expected_padded_len_8)

        # sequence length of 9
        encoded_text_len_9 = "101010101"
        expected_padded_len_9 = "000001111010101010000000"
        self.assertEqual(self.Huffman.pad_encoded_sequence(encoded_text_len_9), expected_padded_len_9)


    def test_output_binary(self):
        padded_sequence_long = "110101010101010100000011"
        expected_binary_output_long = bytearray(b'\xd5U\x03')
        self.assertEqual(self.Huffman.output_binary(padded_sequence_long), expected_binary_output_long)


    
    def test_cut_padding(self):
        padded_sequence = "000000010110101010101010100000011"
        expected_cut_sequence = "011010101010101010000001"
        self.assertEqual(self.Huffman.cut_padding(padded_sequence), expected_cut_sequence)

        padded_sequence_not_start = "10101010000000111110000000"
        expected_cut_sequence_not_start = ""
        self.assertEqual(self.Huffman.cut_padding(padded_sequence_not_start), expected_cut_sequence_not_start)


    def test_decode_content(self):
        # Initialize HuffmanCompress object
        huffman = HuffmanCompress()
        huffman.reverse_mapping = {
            '00': 'a',
            '01': 'b',
            '10': 'c'
        }

        # Test with a simple encoded bit sequence
        encoded_data_simple = "00011001"  # Decodes to "abc"
        expected_decoded_text_simple = "abcb"
        self.assertEqual(huffman.decode_content(encoded_data_simple), expected_decoded_text_simple)

    def tearDown(self):
        if os.path.exists(self.compressed_file_path):
            os.remove(self.compressed_file_path)
        if os.path.exists(self.decompressed_file_path):
            os.remove(self.decompressed_file_path)