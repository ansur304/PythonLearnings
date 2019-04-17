def print_dup_removed(in_list):
    out_list = []
    for x in in_list:
        if not out_list.__contains__(x):
            out_list.append(x)
    print(out_list)


def find_max_sort(in_list):
    return 0#in_list[in_list.-1]


def find_max_loop(in_list):
    print(in_list)
    maximum = int(in_list[0])
    for i in in_list:
        if i > maximum:
            maximum = i
    return maximum


def find_min(in_list):
    return in_list[0]


def read_input():
    in_list = []
    i = 0
    number = int(input("Enter the size of list :: "))
    print("Enter the numbers in list ::")
    while i < number:
        in_list.append(int(input()))
        i = i + 1
    print(f"input List :: %s " % in_list)
    return sorted(in_list)

# coordinates = (1, 2, 3)
# x, y, z = coordinates
#
# print(x, y, z)