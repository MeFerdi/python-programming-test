def max_distinct_gifts(arr):
    table_indices = {}
    max_gits = 0
    start_index = 0

    for i in range(len(arr)):
        gift = arr[i]

        if gift in table_indices and table_indices[gift] >= start_index:

            start_index = table_indices[gift] + 1

            table_indices[gift] = i

            max_gifts = max(max_gifts, i - start_index + 1)

            return max_gifts