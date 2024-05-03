import unittest
import io
from unittest.mock import patch, ANY
from file_utils import list_files
from ui import display_file_lists, display_compression_stats, display_decompression_stats

class TestDisplayFunctions(unittest.TestCase):

    @patch('ui.list_files')
    def test_display_file_lists(self, mock_list_files):
        mock_list_files.side_effect = [  # Simulate different scenarios
            (["file1.txt", "file2.txt"], ["file1.bin"]),
            ([], []),
            (["file1.txt"], ["file1.bin", "file2.bin"]),
            ([], ["file1.bin", "file2.bin"])
        ]

        with patch('builtins.print') as mocked_print:
            display_file_lists()
            mocked_print.assert_called()

    def test_display_compression_stats(self):
        with patch('builtins.print') as mocked_print:
            display_compression_stats("LZ77", 1000, 500, 0.5)
            mocked_print.assert_called()

    def test_display_decompression_stats(self):
        with patch('builtins.print') as mocked_print:
            display_decompression_stats("LZ77", 0.2)
            mocked_print.assert_called()