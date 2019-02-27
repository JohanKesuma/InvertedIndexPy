from operator import attrgetter

from model.document import Document
from model.term import Term
from model.posting import Posting
from model.search import Search
import copy


class InvertedIndex(object):

    def __init__(self):
        self.dictionary = []  # list of Term()

        self.documents = []  # list of Document()

    def addNewDocument(self, document):
        self.documents.append(document)

    def getDocumentSize(self):
        return len(self.documents)

    def getUnsortedIndex(self):
        # isi postingList
        postingList = []
        for doc in self.documents:
            docTerm = doc.content.split(" ")
            for t in docTerm:
                posting = Posting(t.lower(), doc)
                postingList.append(posting)
        # end

        return postingList

    def getSortedIndex(self):
        postingList = self.getUnsortedIndex()
        postingList.sort(key=attrgetter('term'))
        return postingList

    def searchOneWord(self, word):

        if len(self.dictionary) == 0:
            # jika dictionary kosong, return list kosong
            return []
        else:
            pos = Search.binarySearch(self.dictionary, word.lower(), 'term')
            if pos >= 0:
                return self.dictionary[pos].postingList.postingList
            # end if

            # jika data tidak ada maka return list kosong
            return [] 
        # end if

    def makeDictionary(self):

        tempTerms = self.getSortedIndex()

        term1 = Term()
        for i in range(len(tempTerms)):

            term1.term = tempTerms[i].term

            if i > 0:
                if tempTerms[i].term == tempTerms[i - 1].term:
                    if tempTerms[i].document.docId != tempTerms[i - 1].document.docId:
                        posting = tempTerms[i]
                        term1.postingList.postingList.append(posting)
                else:
                    posting = tempTerms[i]
                    term1.postingList.postingList.append(posting)
            else:
                posting = tempTerms[i]
                term1.postingList.postingList.append(posting)
            if i < (len(tempTerms) - 1):
                if tempTerms[i].term != tempTerms[i + 1].term:
                    self.dictionary.append(copy.deepcopy(term1))
                    term1.postingList.postingList.clear()
            else:
                self.dictionary.append(copy.deepcopy(term1))
        # end

    def searchWordIndictionary(self, word):
        for i in range(len(self.dictionary)):
            if self.dictionary[i].term == word:
                return i

        return -1

    def __str__(self):
        string = ''
        for x in self.dictionary:
            string += x.__str__()
            string += '\n'

        return string
