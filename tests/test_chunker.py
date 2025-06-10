from code_rag.code_chunker import CodeChunker

def test_chunk_code_basic():
    chunker = CodeChunker()
    code = '''
    public class Foo {
        public void Bar() {}
        private int Baz() { return 42; }
    }
    '''
    chunks = chunker.chunk_code(code)
    assert any("Bar" in c for c in chunks)