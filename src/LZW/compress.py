class LZWCompressor:
    def compress(self, input_file, output_file):
        lzw_dictionary = {}
        for i in range(256):
            lzw_dictionary[chr(i)] = i

        next_code = 256

        with open(input_file, 'r', encoding='ASCII') as file_open:
            data = file_open.read()

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

        print("compressed data:", compressed_section)

        with open(output_file, 'wb') as output:
            for char in compressed_section:
                output.write(char.to_bytes(2, "big"))

        print("Compressed data saved to", output_file)
