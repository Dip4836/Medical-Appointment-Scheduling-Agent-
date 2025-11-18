from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SimpleRetriever:
    def __init__(self, docs: dict):
        # docs: {key: text}
        self.keys = list(docs.keys())
        self.docs = [docs[k] for k in self.keys]
        self.vectorizer = TfidfVectorizer().fit(self.docs)
        self.doc_vectors = self.vectorizer.transform(self.docs)

    def retrieve(self, query: str, k: int = 3):
        qv = self.vectorizer.transform([query])
        sims = cosine_similarity(qv, self.doc_vectors)[0]
        idx = list(np.argsort(sims)[::-1][:k])
        return [(self.keys[i], self.docs[i], float(sims[i])) for i in idx]