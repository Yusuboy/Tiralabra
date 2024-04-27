class LZWCompressor:
    """
    Class for compressing natural language containing text file using the LZW compressing algorithm
    """

    def __init__(self):
        """
        Initializes the LZWCompressor object.
        """
        self.lzw_dictionary = {}
        for code_point in range(0x110000):  # Iterate over all Unicode code points
            char = chr(code_point)
            self.lzw_dictionary[char] = code_point
        self.next_code = 0x110000

    def _read_input_file(self, input_file):
        """
        Reads data from the input file.

        Args:
            input_file (str): The path to the file we want to compress.

        Returns:
            str: The content of the input file.
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as file_open:  # Changed encoding to UTF-8
                data = file_open.read()
            return data
        except FileNotFoundError:
            raise FileNotFoundError("Input file not found.")

    def _compress_data(self, data):
        """
        Compresses the input data using the LZW algorithm.

        Args:
            data (str): The data to be compressed.

        Returns:
            list: The compressed data.
        """
        compressed_section = []
        sequence = ""
        for char in data:
            if sequence + char in self.lzw_dictionary:
                sequence += char
            else:
                compressed_section.append(self.lzw_dictionary[sequence])
                self.lzw_dictionary[sequence + char] = self.next_code
                self.next_code += 1
                sequence = char

        if sequence in self.lzw_dictionary:
            compressed_section.append(self.lzw_dictionary[sequence])

        return compressed_section

    def _write_output_file(self, compressed_data, output_file):
        """
        Writes the compressed data to the output file.

        Args:
            compressed_data (list): The compressed data.
            output_file (str): The path to the output file where the compressed data will be saved.

        Returns:
            None
        """
        with open(output_file, 'wb') as output:
            for char in compressed_data:
                output.write(char.to_bytes(4, "big"))

        # print("Compressed data saved to", output_file)

    def compress(self, input_file, output_file):
        """
        Compresses data from a input file and saves the compressed data in the output file.

        Args:
            input_file (str): The path to the file we want to compress.
            output_file (str): The path to the output file where the compressed data will be saved.

        Returns:
            None
        """
        data = self._read_input_file(input_file)
        compressed_data = self._compress_data(data)
        self._write_output_file(compressed_data, output_file)
