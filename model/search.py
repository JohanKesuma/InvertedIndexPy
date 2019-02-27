class Search(object):
    @staticmethod
    def binarySearch(data, key):

        # init index low, mid, dan high
        indexLow = 0
        indexHigh = len(data) - 1

        for i in range(len(data)):
            
            indexMid = (indexHigh + indexLow) / 2
            indexMid = int(indexMid)

            if data[indexMid] != key and i == (len(data) - 1):
                print('data tidak ketemu')
                return -1
            elif data[indexMid] == key:
                return indexMid
            elif data[indexMid] > key:
                indexHigh = indexMid - 1
            else:
                indexLow = indexMid + 1
                
        # end for

    # end binary search
