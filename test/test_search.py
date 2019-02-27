from sys import path
path.append('.')

from model.document import Document
from model.search import Search

if __name__ == "__main__":
    doc1 = Document(
        "1", "Candi Prambanan merupakan salah satu candi yang ada di Indonesia")
    doc2 = Document(
        "2", "Indonesia Merupakan Negara Yang Mempunyai Banyak Candi")
    doc3 = Document("3", "Liburan di Negara Berkembang")

    docs = [doc1, doc2, doc3]

    pos = Search.binarySearch(docs, "1", 'docId')

    print(pos)

