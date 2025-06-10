"""
Vector index for code embeddings.
"""
import faiss
import numpy as np

class FaissIndex:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.embeddings = []
        self.metadata = []

    def add(self, embedding, meta):
        x = np.array([embedding]).astype(np.float32)
        self.index.add(x)
        self.embeddings.append(embedding)
        self.metadata.append(meta)

    def search(self, embedding, k=5):
        D, I = self.index.search(np.array([embedding]).astype(np.float32), k)
        return [(self.metadata[i], float(D[0][j])) for j, i in enumerate(I[0])]