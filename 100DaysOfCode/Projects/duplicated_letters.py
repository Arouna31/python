# This program finds duplicated letters in a list without using sets
some_list = ["a", "b", "c", "b", "d", "m", "n", "n", "n"]
duplicated_items = []
list_len = len(some_list)

i = 0
while i < list_len:
    process_letter = some_list[i]
    print(process_letter)
    for letter in some_list[i + 1 :]:
        print(letter, end=", ")
        if letter == process_letter and not letter in duplicated_items:
            duplicated_items.append(process_letter)
    i = i + 1

print("The duplicated letters are", end=": ")
for letter in duplicated_items:
    print(letter, end=" ")
