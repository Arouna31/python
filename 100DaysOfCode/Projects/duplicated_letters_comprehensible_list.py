# This program finds duplicated letters in a list without using sets
some_list = ["a", "b", "c", "b", "d", "m", "n", "n", "n"]

duplicated_items = list(set([item for item in some_list if some_list.count(item) > 1]))

print(duplicated_items)
