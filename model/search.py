class Search(object):
    @staticmethod
    def binarySearch(data, key, attr=None):

        # init index low, mid, dan high
        indexLow = 0
        indexHigh = len(data) - 1

        if attr == None:
            for i in range(len(data)):

                indexMid = (indexHigh + indexLow) / 2
                indexMid = int(indexMid)

                if data[indexMid] != key and i == (len(data) - 1):
                    # data tidak ada
                    return -1
                elif data[indexMid] == key:
                    return indexMid
                elif data[indexMid] > key:
                    indexHigh = indexMid - 1
                else:
                    indexLow = indexMid + 1

            # end for
        else:
            for i in range(len(data)):

                indexMid = (indexHigh + indexLow) / 2
                indexMid = int(indexMid)

                if eval('data[indexMid].'+ attr) != key and i == (len(data) - 1):
                    # data tidak ada
                    return -1
                elif eval('data[indexMid].'+ attr) == key:
                    return indexMid
                elif eval('data[indexMid].'+ attr) > key:
                    indexHigh = indexMid - 1
                else:
                    indexLow = indexMid + 1

            # end for
        # end if

    # end binary search
