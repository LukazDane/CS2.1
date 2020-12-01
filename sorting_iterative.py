#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) just checks original list the once
    TODO: Memory usage: O(n) no additional space neded to check the list"""
    # TODO: Check that all adjacent items are in order, return early if so
    if (items == sorted(items)):
        return True
    else:
        return False


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) if it has to swap every pair | O(n) already sorted
    TODO: Memory usage: O(1) sorting occurs in allocated space and does not increase/decrease in proportion to the inputs"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    print("Original: "+str(items))
    while is_sorted(items) is False:

        for i in range(len(items)-1):  # go through each item in array
            if items[i] > items[i+1]:  # Compare pairs
                # switch around if pairs not in correct order
                items[i], items[i+1] = items[i+1], items[i]
                is_sorted(items)
    print("Bubble Sorted: " + str(items) + "\n")


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) nested loops
    TODO: Memory usage: O(1) only uses as much space as the list already occupies and does not make unnecessary swaps"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    print("Original: "+str(items))
    while is_sorted(items) is False:

        for i in range(len(items)-1):
            min = i  # set a minimum i
            for j in range(i+1, len(items)):
                if items[min] > items[j]:  # adjust minimum if current is larger than next item
                    min = j
            # swap em around
            temp = items[i]
            items[i] = items[min]
            items[min] = temp
    print("Selection Sorted: " + str(items) + "\n")


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n) already sorted | O(n^2) if list is in reverse sorted order
    TODO: Memory usage: O(1) swaps/inserting occurs inplace """
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    # print("Original: "+str(items))
    while is_sorted(items) is False:
        for i in range(1, len(items)):
            x = items[i]
            y = i

            while y >= 0 and items[y - 1] > x:  # grab unsorted i
                items[y] = items[y - 1]
                y = y - 1

            items[y] = x  # insert
    return str(items)


# items = [4, 8, 2, 16, 64, 32]
# items2 = [2, 4, 8, 16, 32, 64]
# print(is_sorted(items))
# bubble_sort(items)
# bubble_sort(items2)
# selection_sort(items)
# selection_sort(items2)
# insertion_sort(items)
# insertion_sort(items2)
