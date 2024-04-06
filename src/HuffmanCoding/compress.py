import heapq
from HuffmanCoding.heap_node import HeapNode

class HuffmanCompress:
    def __init__(self):
        self.heap = []
        self.nodes = {}


    def frequency_dictionary(self, text):
        frequency = {}
        for i in text:
            if i not in frequency:
                frequency[i] = 0
            frequency[i] += 1
        return frequency


    def build_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)


    def merge_nodes(self): 
        while len(self.heap)>1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)



    def make_nodes_helper(self, node, current_sequence):
        if(node == None):
            return
        
        if(node.char != None):
            self.nodes[node.char] = current_sequence

        self.make_nodes_helper(node.left, current_sequence + "0")
        self.make_nodes_helper(node.right, current_sequence + "1")

    def make_nodes(self):
        root =  heapq.heappop(self.heap)
        current_sequence = ""
        self.make_nodes_helper(root, current_sequence)

    def encode_text(self, data):
        encoded_text = ""
        for i in data:
            encoded_text += self.nodes[i]
        return encoded_text

    def pad_encoded_sequence(self, encoded_text):
        padding = 8 - len(encoded_text) % 8
        for i in range(padding):
            encoded_text += "0"

        padded_data = "{0:08b}".format(padding)
        encoded_text = padded_data + encoded_text
        return encoded_text


    def output_binary(self, padded_sequence):
        b = bytearray()
        for i in range(0, len(padded_sequence), 8):
            byte = padded_sequence[i:i+8]
            b.append(int(byte,2))
        return b

    def compress(self, input_file, output_file):
        try:
            with open(input_file, 'r+', encoding='utf-8') as file_open:
                data = file_open.read()
                data = data.rstrip()
        except ValueError:
            pass

        frequency = self.frequency_dictionary(data)
        print(frequency)

        self.build_heap(frequency)
        self.merge_nodes()
        self.make_nodes()
        
        encoded_text = self.encode_text(data)
        padded_sequence = self.pad_encoded_sequence(encoded_text)

        code = self.output_binary(padded_sequence)
        with open(output_file, 'wb') as output:
            output.write(bytes(code))
    print("Compressed")