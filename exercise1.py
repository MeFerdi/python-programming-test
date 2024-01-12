from collections import Counter

def find_modes(1st)

counter = Counter(1st)

max_count = max(counter.value())#Finding maximum count

modes = [key for key, value in counter.items() if value == max_count]#getting all elements with maximum count

return modes