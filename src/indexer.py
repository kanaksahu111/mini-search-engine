def build_index(documents, tokenize):
    index = {}

    for doc, text in documents.items():
        for word in tokenize(text):
            index.setdefault(word, set()).add(doc)

    return index
