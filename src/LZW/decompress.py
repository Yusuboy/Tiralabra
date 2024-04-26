class LZWDecompressor:
    """
    Class for decompressing data using LZW decompression algorithm
    """

    def __init__(self):
        """
        Initializes the LZWDecompressor object.
        """
        self.lzw_dictionary = dict([(x, chr(x)) for x in range(0x110000)])
        self.next_code = 0x110000

    def _read_compressed_data(self, input_file):
        """
        Reads compressed data from the input file.

        Args:
            input_file (str): The path to the file containing compressed data.

        Returns:
            list: The list of compressed data.
        """
        try:
            with open(input_file, "rb") as compressed_file:
                compressed_data = []
                while True:
                    bytes_read = compressed_file.read(4)
                    if len(bytes_read) != 4:
                        break
                    data = int.from_bytes(bytes_read, byteorder='big')
                    compressed_data.append(data)
                return compressed_data
        except FileNotFoundError:
            raise FileNotFoundError("Input file not found.")

    def _decompress_data(self, compressed_data):
        """
        Decompresses the input data using the LZW decompression algorithm.

        Args:
            compressed_data (list): The compressed data to be decompressed.

        Returns:
            str: The decompressed data.
        """
        decompressed_section = ""
        sequence = ""
        for byte in compressed_data:
            if byte not in self.lzw_dictionary:
                self.lzw_dictionary[byte] = sequence + sequence[0]

            decompressed_section += self.lzw_dictionary[byte]

            if len(sequence) != 0:
                self.lzw_dictionary[self.next_code] = sequence + self.lzw_dictionary[byte][0]
                self.next_code += 1
            sequence = self.lzw_dictionary[byte]
        return decompressed_section

    def _write_output_file(self, decompressed_data, output_file):
        """
        Writes the decompressed data to the output file.

        Args:
            decompressed_data (str): The decompressed data.
            output_file (str): The path to the output file where the decompressed data will be saved.

        Returns:
            None
        """
        with open(output_file, 'w', encoding='utf-8') as output:  # Changed encoding to UTF-8
            output.write(decompressed_data)

        print("Decompressed data saved to", output_file)

    def decompress(self, input_file, output_file):
        """
        Decompresses data from an input file and saves the decompressed data to the output file.

        Args:
            input_file (str): The path to the file containing compressed data.
            output_file (str): The path to the output file where the decompressed data will be saved.

        Returns:
            None
        """
        compressed_data = self._read_compressed_data(input_file)
        decompressed_data = self._decompress_data(compressed_data)
        self._write_output_file(decompressed_data, output_file)
