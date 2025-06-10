"""
BM25 implementation for code search.
"""
from rank_bm25 import BM25Okapi

class BM25Index:
    def __init__(self, documents):
        self.tokenized_docs = documents
        self.bm25 = BM25Okapi(self.tokenized_docs)

    def get_scores(self, tokenized_query):
        return self.bm25.get_scores(tokenized_query)

    def get_top_n(self, tokenized_query, n=5):
        return self.bm25.get_top_n(tokenized_query, self.tokenized_docs, n=n)