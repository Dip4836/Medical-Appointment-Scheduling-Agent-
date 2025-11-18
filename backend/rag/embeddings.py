
try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    model = SentenceTransformer('all-MiniLM-L6-v2')
    def embed_texts(texts):
        return model.encode(texts, convert_to_numpy=True)
except Exception:
    def embed_texts(texts):
        return [[float(sum(bytearray(t.encode("utf-8")))%1000)/1000.0] for t in texts]