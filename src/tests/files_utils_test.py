import unittest
import os
from file_utils import is_txt_file, get_file_size, list_files, delete_files_in_folder

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.test_text_file = "test.txt"
        self.test_binary_file = "test.bin"
        with open(self.test_text_file, "w") as f:
            f.write("This is a test text file.")
        with open(self.test_binary_file, "wb") as f:
            f.write(b"This is a test binary file.")


    def tearDown(self):
        if os.path.exists(self.test_text_file):
            os.remove(self.test_text_file)
        if os.path.exists(self.test_binary_file):
            os.remove(self.test_binary_file)

    def test_is_txt_file(self):
        self.assertTrue(is_txt_file(self.test_text_file))
        self.assertFalse(is_txt_file(self.test_binary_file))

    def test_get_file_size(self):
        self.assertEqual(get_file_size(self.test_text_file), os.path.getsize(self.test_text_file))
        self.assertEqual(get_file_size(self.test_binary_file), os.path.getsize(self.test_binary_file))

    def test_list_files(self):
        text_files = list_files(".", ".txt")

        self.assertIn(self.test_text_file, text_files)
        binary_files = list_files(".", ".bin")
        self.assertIn(self.test_binary_file, binary_files)

    # def test_delete_files_in_folder(self):
    #     delete_files_in_folder(".")

    #     self.assertFalse(os.path.exists(self.test_text_file))
    #     self.assertFalse(os.path.exists(self.test_binary_file))