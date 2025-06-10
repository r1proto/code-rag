from ../src/code_rag.tokenizer import EnhancedCSharpTokenizer

def test_tokenization_basic():
    tokenizer = EnhancedCSharpTokenizer()
    code = "public class UserAuthService { public void Login() {} }"
    tokens = tokenizer._tokenize_code(code)
    assert "user" in tokens and "auth" in tokens and "login" in tokens