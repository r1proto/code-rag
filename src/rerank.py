"""
Reranking logic for hybrid search results.
"""

class SimpleReranker:
    def rerank(self, candidates, query_embedding, scoring_fn=None):
        # Optionally rerank using a custom scoring function
        # Default: return as is
        if scoring_fn:
            return sorted(candidates, key=lambda c: scoring_fn(query_embedding, c[0]), reverse=True)
        return candidates