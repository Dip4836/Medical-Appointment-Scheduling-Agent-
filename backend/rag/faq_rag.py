import json
import os
from .vector_store import SimpleRetriever

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "clinic_info.json")

class FAQRAG:
    def __init__(self):
        with open(DATA_PATH, "r") as f:
            self.docs = json.load(f)
        # flatten to key -> text
        flat = {}
        for k, v in self.docs.items():
            flat[k] = v
        self.retriever = SimpleRetriever(flat)

    def get_answers(self, query: str, k: int = 3):
        results = self.retriever.retrieve(query, k=k)
        # return list of text answers
        return [{"source": r[0], "text": r[1], "score": r[2]} for r in results]