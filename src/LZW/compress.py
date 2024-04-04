class LZWCompressor:
    """
    Class for compressing natural language containing text file using the LZW compressing algorithm

    Attributes:
        None

    """
    def compress(self, input_file, output_file):
        """
        Compresses data from a input file and saves the compressed data in the output file.

        Args:
            input_file (str): The path to the file we want to compress.
            output_file (str): The path to the output file where the compressed data will be saved.

        Returns:
            None

        Raises:
            FileNotFoundError: If the input file does not exist.
        """
        lzw_dictionary = {}

        for code_point in range(0x110000):  # Iterate over all Unicode code points
            try:
                char = chr(code_point)
                lzw_dictionary[char] = code_point
            except ValueError:
                pass

        next_code = 0x110000
        try:
            with open(input_file, 'r', encoding='utf-8') as file_open:  # Changed encoding to UTF-8
                data = file_open.read()
        except FileNotFoundError:
            raise FileNotFoundError("Input file not found.")

        compressed_section = []
        sequence = ""
        for char in data:
            if sequence + char in lzw_dictionary:
                sequence = sequence + char
            else:
                compressed_section.append(lzw_dictionary[sequence])
                lzw_dictionary[sequence + char] = next_code
                next_code += 1
                sequence = char

        if sequence in lzw_dictionary:
            compressed_section.append(lzw_dictionary[sequence])

        # print("compressed data:", compressed_section)

        with open(output_file, 'wb') as output:
            for char in compressed_section:
                output.write(char.to_bytes(4, "big"))

        print("Compressed data saved to", output_file)
