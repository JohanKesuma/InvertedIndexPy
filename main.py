from model.document import *

if __name__ == "__main__":
    document = []
    document.append(Document(
        "1", "Candi Prambanan merupakan salah satu candi yang ada di Indonesia"))
    document.append(
        Document("2", "Indonesia Merupakan Negara Yang Mempunyai Banyak Candi"))
    document.append(Document("3", "Liburan di Negara Berkembang"))

    doc = Document()

    for doc in document:
        print(doc.docId + " -> " + doc.content)

    print("=======")
    print("Terms : ")

    terms = []

    for doc in document:
        docTerm = doc.content.split(" ")
        for term in docTerm:
            terms.append(term)

    terms = sorted(terms)

    for i in range(len(terms)):
        print(str(terms[i]).lower())