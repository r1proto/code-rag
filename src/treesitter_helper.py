from tree_sitter import Language, Parser
import os

class CSharpTreeSitter:
    def __init__(self, so_path=None):
        so_path = so_path or os.getenv("TS_CSHARP_SO", "build/my-languages.so")
        self.lang = Language(so_path, "c_sharp")
        self.parser = Parser()
        self.parser.set_language(self.lang)

    def parse_code(self, code: str):
        return self.parser.parse(bytes(code, "utf8"))

    def extract_methods(self, code: str):
        tree = self.parse_code(code)
        root = tree.root_node
        methods = []
        # Traverse the tree and extract 'method_declaration' nodes
        cursor = root.walk()
        stack = [cursor.node]
        while stack:
            node = stack.pop()
            if node.type == "method_declaration":
                methods.append(code[node.start_byte:node.end_byte])
            stack.extend(node.children)
        return methods