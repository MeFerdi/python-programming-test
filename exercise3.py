def getDistinctElements(A):
    return list(set(A))

def getSubarray(A, start, end):
    return A[start - 1:end]

def isArrayContained(A, B):
    return all(elem in A for elem in B)

def minTablesToGrabDistinctGifts(A):
    min_tables = float('inf')
    distinct_gifts = getDistinctElements(A)

    for i in range(len(A)):
        for j in range(i, len(A)):
            subarray = getSubarray(A, i + 1, j + 1)
            if len(getDistinctElements(subarray)) == len(distinct_gifts) and isArrayContained(subarray, distinct_gifts):
                min_tables = min(min_tables, j - i + 1)

    return min_tables
