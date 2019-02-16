from operator import attrgetter

from model.document import *
from model.inverted_index import InvertedIndex
from model.term import Term

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
        print(doc.docId + " -> " + doc.content) # menampilkan konten dokumen
    # end iterate



    print("=======")
    print("Terms : ")
    print()

    # # isi list term
    # tempTerms = []
    # for doc in document:
    #     docTerm = doc.content.split(" ")
    #     for t in docTerm:
    #         term = Term(t, doc)
    #         tempTerms.append(term)
    # # end

    # # menampilkan semua object term
    # for t in tempTerms:
    #     print(t)
    # # end

    # tempTerms.sort(key = attrgetter('term'))

    # print('========')
    # print('sorted')
    # print('')

    # for t in tempTerms:
    #     print(t)

    iIndex = InvertedIndex.toInvertedIndex(document)
    print(iIndex)
