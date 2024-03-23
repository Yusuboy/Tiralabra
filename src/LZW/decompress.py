class LZWDecompressor:
    """
    Class for decompressing data using LZW decomresss algorithm

    Attributes:
        None
    """
    def decompress(self, input_file, output_file):
        """Decompresses data from a input file and saves the decompressed data to the output file.

        Args:
            input_file (str): The path to the file containing compressed data.
            output_file (str): The path to the output file where,
            the decompressed data will be saved.

        Return:
            None

        Raises:
            FileNotFoundError: If the input file does not exist.
        """
        lzw_dictionary = dict([(x, chr(x)) for x in range(256)])
        next_code = 256

        try:
            compressed_data = open(input_file, "rb")
        except FileNotFoundError:
            raise FileNotFoundError("Input file not found.")

        compressed_section = []
        decompressed_section = ""
        sequence = ""

        while True:
            # Read two bytes from the file
            bytes_read = compressed_data.read(2)
            # Check if both bytes were successfully read
            if len(bytes_read) != 2:
                # If either byte is missing, it means we've reached the end of the file
                break
            # Convert the bytes to a 16-bit integer
            data = int.from_bytes(bytes_read, byteorder='big')
            # Append the integer to the list
            compressed_section.append(data)

        for byte in compressed_section:
            # sequences += chr(byte)
            if byte not in lzw_dictionary:
                lzw_dictionary[byte] = sequence + (sequence[0])

            decompressed_section += lzw_dictionary[byte]

            if len(sequence) != 0:
                lzw_dictionary[next_code] = sequence + lzw_dictionary[byte][0]
                next_code+=1
            sequence = lzw_dictionary[byte]


        with open(output_file, 'w', encoding='ASCII') as output:
            output.write(decompressed_section)

        print("Decompressed data saved to", output_file)
