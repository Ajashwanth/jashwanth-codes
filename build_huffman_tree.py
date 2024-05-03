class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

def build_huffman_tree(decode_text):
    nodes = [Node(freq, char) for char, freq in decode_text.items()]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged = Node(left.freq + right.freq)
        merged.left = left
        merged.right = right
        nodes.append(merged)
    return nodes[0]

def encode_huffman_tree(root, prefix="", code_map={}):
    if root is None:
        return code_map
    if root.char is not None:
        code_map[root.char] = prefix
    encode_huffman_tree(root.left, prefix + "0", code_map)
    encode_huffman_tree(root.right, prefix + "1", code_map)
    return code_map

# Example usage:
text = "this is example of huffman code"
decode_text = {}
for char in text:
    decode_text[char] = decode_text.get(char, 0) + 1

huffman_tree = build_huffman_tree(decode_text)
huffman_codes = encode_huffman_tree(huffman_tree)

print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(f"{char}: {code}")
