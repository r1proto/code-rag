from code_rag.index import FaissIndex
import numpy as np

def test_index_basic():
    idx = FaissIndex(dim=4)
    emb1 = np.array([1, 0, 0, 0], dtype=np.float32)
    emb2 = np.array([0, 1, 0, 0], dtype=np.float32)
    idx.add(emb1, {"id": 1})
    idx.add(emb2, {"id": 2})
    results = idx.search(emb1, k=1)
    assert results[0][0]["id"] == 1