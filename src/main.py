from document_loader import load_documents
from tokenizer import tokenize
from indexer import build_index
from search import search

DATA_FOLDER = "../data"

def main():
    print("Mini Search Engine Started")

    documents = load_documents(DATA_FOLDER)
    build_index(documents, tokenize)

    while True:
        query = input("\nSearch (or type exit): ")

        if query.lower() == "exit":
            break

        results = search(query, documents)

        if not results:
            print("No results found")
        else:
            for r in results:
                print(f"{r['document']} | score {r['score']} | {r['sentence']}")

if __name__ == "__main__":
    main()
