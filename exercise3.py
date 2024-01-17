def min_tables_to_grab_gifts(gifts):
    gift_positions = {}
    max_gift_count = 0
    start_table = 0
    end_table = 0

    current_start = 0
    current_gift_count = 0

    for i, gift in enumerate(gifts):
        if gift in gift_positions and gift_positions[gift] >= current_start:
            current_start = gift_positions[gift] + 1
            current_gift_count = i - current_start

        gift_positions[gift] = i
        current_gift_count += 1

        if current_gift_count > max_gift_count:
            max_gift_count = current_gift_count
            start_table = current_start
            end_table = i

    return start_table, end_table, gifts[start_table:end_table+1]
