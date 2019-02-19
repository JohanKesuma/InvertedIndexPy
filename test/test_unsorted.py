import sys
sys.path.append('.')
from operator import attrgetter

from model.document import Document
from model.inverted_index import InvertedIndex

if __name__ == "__main__":
    doc1 = Document(
        "1", "Candi Prambanan merupakan salah satu candi yang ada di Indonesia")
    doc2 = Document(
        "2", "Indonesia Merupakan Negara Yang Mempunyai Banyak Candi")
    doc3 = Document("3", "Liburan di Negara Berkembang")

    invertedIndex = InvertedIndex()

    invertedIndex.addNewDocument(doc1)
    invertedIndex.addNewDocument(doc2)
    invertedIndex.addNewDocument(doc3)

    for x in invertedIndex.getUnsortedIndex():
        print(x.term + ' -> ' + x.document.docId)
