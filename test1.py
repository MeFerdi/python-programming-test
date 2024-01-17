list1 = [1, 5, 2, 6, 2, 3, 3, 2, 8, 2]
list2 = [500, -100, 200, 50, -100, 300, 50, 700, 50, -100, 500]

modes_list1, count_list1 = find_modes(list1)
modes_list2, count_list2 = find_modes(list2)

print("Modes in List1:", modes_list1, "with count:", count_list1)
print("Modes in List2:", modes_list2, "with count:", count_list2)
