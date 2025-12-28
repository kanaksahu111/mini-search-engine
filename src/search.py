from tokenizer import tokenize
import re

def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text)

def highlight(sentence, tokens):
    for t in tokens:
        sentence = re.sub(
            rf"({re.escape(t)})",
            r"<mark>\1</mark>",
            sentence,
            flags=re.IGNORECASE
        )
    return sentence

def search(query, documents):
    query_tokens = tokenize(query)
    results = []

    for doc, content in documents.items():
        for sentence in split_sentences(content):
            words = tokenize(sentence)
            score = sum(words.count(t) for t in query_tokens)

            if score > 0:
                results.append({
                    "document": doc,
                    "sentence": highlight(sentence, query_tokens),
                    "score": score
                })

    return sorted(results, key=lambda x: x["score"], reverse=True)
