def max_distinct_gifts(arr):
    gift_index = {}
    start = max_distinct = 0

    for end, gift in enumerate(arr):
        start = max(start, gift_index.get(gift, 0) + 1)
        gift_index[gift] = end
        max_distinct = max(max_distinct, end - start + 1)

    return max_distinct
