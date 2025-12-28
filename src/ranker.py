def rank_documents(query_tokens, documents):
    scores = {}

    for doc, text in documents.items():
        words = text.lower().split()
        score = sum(words.count(token) for token in query_tokens)

        if score > 0:
            scores[doc] = score

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
