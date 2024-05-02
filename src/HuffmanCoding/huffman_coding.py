import heapq


class HuffmanCompress:
        """Implements Huffman coding compression and decompression."""
        def __init__(self):
            """Initialize HuffmanCompress object."""
            self.heap = []
            self.nodes = {}
            self.reverse_mapping = {}


        class HeapNode:
            """
            Class representing nodes in the Huffman tree.
            """
            def __init__(self, char, freq):
                """
                Initialize HeapNode object.

                Parameters:
                    char (str): Character represented by the node.
                    freq (int): Frequency of the character.
                """
                self.char = char
                self.freq = freq
                self.left = None
                self.right = None

            def __lt__(self, other):
                """
                Less than comparison operator for HeapNode objects.
                """
                return self.freq < other.freq

            def __eq__(self, other):
                """
                Equel than comparison operator for HeapNode objects.
                """
                if(other == None):
                    return False
                return self.freq == other.freq

        def frequency_dictionary(self, text):
            """
            Generate frequency dictionary for characters in the text.

            Parameters:
                text (str): Input text.

            Returns:
                dict: Frequency dictionary for characters in the text.
            """
            frequency = {}
            for i in text:
                if not i in frequency:
                    frequency[i] = 0
                frequency[i] += 1
            return frequency


        def build_heap(self, frequency):
            """
            Build a heap based on frequencies.

            Parameters:
                frequency (dict): Frequency dictionary for chars in the text.
            """
            for key in frequency:
                    node = self.HeapNode(key, frequency[key])
                    heapq.heappush(self.heap, node)


        def merge_nodes(self): 
            """
            Merge nodes in the heap to create Huffman tree.
            """
            while(len(self.heap)>1):
                node1 = heapq.heappop(self.heap)
                node2 = heapq.heappop(self.heap)

                merged = self.HeapNode(None, node1.freq + node2.freq)
                merged.left = node1
                merged.right = node2

                heapq.heappush(self.heap, merged)



        def make_nodes_helper(self, node, current_sequence):
            """
            Helper function to create encoding nodes.

            Parameters:
                node (HeapNode): Current node in Huffman tree.
                current_sequence (str): Current encoding sequence.
            """
            if(node == None):
                return
            
            if(node.char != None):
                self.nodes[node.char] = current_sequence
                self.reverse_mapping[current_sequence] = node.char
                return

            self.make_nodes_helper(node.left, current_sequence + "0")
            self.make_nodes_helper(node.right, current_sequence + "1")

        def make_nodes(self):
            """
            Create encoding nodes from Huffman tree.
            """
            root =  heapq.heappop(self.heap)
            current_sequence = ""
            self.make_nodes_helper(root, current_sequence)

        def encode_text(self, data):
            """
            Encode text using Huffman encoding.

            Parameters:
                data (str): Input text to be encoded.

            Returns:
                str: Encoded text.
            """
            encoded_text = ""
            for i in data:
                encoded_text += self.nodes[i]
            return encoded_text

        def pad_encoded_sequence(self, encoded_text):
            """
            Pad the encoded sequence to make its length a multiple of 8.

            Parameters:
                encoded_text (str): Encoded text sequence.

            Returns:
                str: Padded encoded text sequence.
            """
            padding = 8 - len(encoded_text) % 8
            for i in range(padding):
                encoded_text += "0"

            padded_data = "{0:08b}".format(padding)
            encoded_text = padded_data + encoded_text
            return encoded_text


        def output_binary(self, padded_sequence):
            """
            Convert padded binary sequence to bytes.

            Parameters:
                padded_sequence (str): Padded binary sequence.

            Returns:
                bytes: Binary representation of the sequence.
            """
            if(len(padded_sequence)%8 != 0):
                print("Encoded text not padded properly")
                exit(0)

            b = bytearray()
            for i in range(0, len(padded_sequence), 8):
                byte = padded_sequence[i:i+8]
                b.append(int(byte,2))
            return b

        def compress(self, input_file, output_file):
            """
            Compres inäut file using Huffman encoding.

            Parameters:
                input_file (str): Path to input file.
                output_file (str): Path to output compressed file.

            Returns:
                str: Path to the compressed output file.
            """

            with open(input_file, 'r') as file_open:
                data = file_open.read()


                frequency = self.frequency_dictionary(data)


                self.build_heap(frequency)
                self.merge_nodes()
                self.make_nodes()

                encoded_text = self.encode_text(data)
                # print(encoded_text)
                # print(type(encoded_text))
                padded_sequence = self.pad_encoded_sequence(encoded_text)
                # print(padded_sequence)
                # print(type(padded_sequence))
                code = self.output_binary(padded_sequence)
                with open(output_file, 'wb') as output:
                    # print(bytes(code))
                    # print(type(bytes(code)))
                    output.write(bytes(code))




        def cut_padding(self, bit_sequence):
            """
            takes the padding from the beginning of a bit sequence off.

            Parameters:
                bit_sequence (str): A string representing a sequence of bits.

            Returns:
                str: The bit sequence with no removed.
            """
            padded_figures = bit_sequence[:8]
            additional_padding = int(padded_figures, 2)

            bit_sequence = bit_sequence[8:]
            encoded_text = bit_sequence[:-1*additional_padding]

            return encoded_text


        def decode_content(self, encoded_data):
            """
            Decodes the an encoded bit sequence into original text.

            Parameters:
                encoded_data (str): A string representing an encoded bit sequence.

            Returns:
                str: The decoded text.
            """
            current_sequence = ""
            decoded_text = ""

            for bit in encoded_data:
                current_sequence += bit
                if current_sequence in self.reverse_mapping:
                    decoded_text += self.reverse_mapping[current_sequence]
                    current_sequence = ""

            return decoded_text


        def decompress(self, input_path, output_path):
            """
            Compres input file using Huffman encoding.

            Parameters:
                input_file (str): Path to input file.
                output_file (str): Path to output compressed file.

            Returns:
                str: Path to the compressed output file.
            """
            with open(input_path, 'rb') as file_open:
                bit_string = ""
                byte = file_open.read(1)
                while len(byte) > 0:
                    byte = ord(byte)
                    bits = bin(byte)[2:].rjust(8, '0')
                    bit_string += bits
                    byte = file_open.read(1)

                encoded_code = self.cut_padding(bit_string)
                decoded_content = self.decode_content(encoded_code)

                with open(output_path, "w") as output_file:
                    output_file.write(decoded_content)


                