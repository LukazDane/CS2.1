#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    result = []
    i1, i2 = 0, 0
    while i1 < len(items1) and i2 < len(items2):
        if items1[i1] < items2[i2]:
            result.append(items1[i1])
            i1 += 1
        else:
            result.append(items2[i2])
            i2 += 1
    if i2 == len(items1):
        result.extend(items2[i2:])
    else:
        result.extend(items1[i1:])
    return result


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: Running time: Always O(n log n)  because it always splits the array in two  and takes linear time to merge them
    TODO: Memory usage: O(n) space because it doesn't need more than O(n) space """
    if len(items) < 2:
        return items
    mid = len(items) // 2  # // int division (rounds down)

    left = items[:mid]
    right = items[mid:]

    items[:] = merge(merge_sort(left), merge_sort(right))
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: 
    TODO: Memory usage:  """
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
