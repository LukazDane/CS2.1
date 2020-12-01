from sorting_iterative import insertion_sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time +  Memory usage: O(n+k) goes through input at least twice, and uses multiple arrays.
    """
    if len(numbers) <= 0:
        return []
    # max_num = max(numbers)+1
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # size = len(numbers)
    # out = [0]*size
    output = [] * len(numbers)
    # TODO: Create list of counts with a slot for each number in input range
    # c = [0]*10
    count = [0]*(max(numbers)+1)
    # TODO: Loop over given numbers and increment each number's count
    # for i in range(0, size):
    #     c[numbers[i]] += 1
    for i in numbers:
        count[i] += 1
    # TODO: Loop over counts and append that many numbers into output list
    for i, j in enumerate(count):
        for x in range(j):
            output.append(i)
    numbers[:] = output

    # for i in range(1, 10):
    #     c[i] += c[i-1]
    # i = size - 1
    # while i >= 0:
    #     out[c[numbers[i]] - 1] = numbers[i]
    #     c[numbers[i]] -= 1
    #     i -= 1
    # for i in range(0, size):
    # numbers[i] = output[i]
    return numbers
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if len(numbers) <= 0:
        return []
    # TODO: Find range of given numbers (minimum and maximum values)
    maximum = max(numbers)
    size = maximum/len(numbers)
    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = []
    for x in range(len(numbers)):
        buckets.append([])
    # TODO: Loop over given numbers and place each item in appropriate bucket
    for i in range(len(numbers)):
        j = int(numbers[i] / size)
        if j != len(numbers):
            buckets[j].append(numbers[i])
        else:
            buckets[len(numbers) - 1].append(numbers[i])
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for z in range(len(numbers)):
        insertion_sort(buckets[z])
    # TODO: Loop over buckets and append each bucket's numbers into output list
    output = []
    for x in range(len(numbers)):
        output = output + buckets[x]
    return output

    # FIXME: Improve this to mutate input instead of creating new output list


data = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(data))
print(counting_sort([]))
print(bucket_sort(data))
print(bucket_sort([]))
