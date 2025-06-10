from .treesitter_helper import CSharpTreeSitter

class CodeChunker:
    def __init__(self):
        self.ts = CSharpTreeSitter()

    def chunk_code(self, code: str):
        # Chunk code by method for now
        return self.ts.extract_methods(code)