from operator import attrgetter

from model.document import Document
from model.inverted_index import InvertedIndex

if __name__ == "__main__":
    document = []
    document.append(Document(
        "1", "Candi Prambanan merupakan salah satu candi yang ada di Indonesia"))
    document.append(
        Document("2", "Indonesia Merupakan Negara Yang Mempunyai Banyak Candi"))
    document.append(Document("3", "Liburan di Negara Berkembang"))

    # iterate doc
    doc = Document()
    for doc in document:
        print(doc.docId + " -> " + doc.content)  # menampilkan konten dokumen
    # end iterate

    print("=======")
    print("Terms : ")
    print()

    iIndex = InvertedIndex.toInvertedIndex(document)
    print(iIndex)
