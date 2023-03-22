def is_anagram(first_string, second_string):
    firstString = list(first_string.lower())
    secondString = list(second_string.lower())

    merge_sort(firstString)
    merge_sort(secondString)

    joinFirst = "".join(firstString)
    joinSecond = "".join(secondString)

    if len(joinFirst) != len(joinSecond):
        return (joinFirst, joinSecond, False)
    if (len(joinFirst) == 0 or len(joinSecond) == 0):
        return (joinFirst, joinSecond, False)

    for i in range(len(joinFirst)):
        if joinFirst[i] != joinSecond[i]:
            return (joinFirst, joinSecond, False)

    return (joinFirst, joinSecond, True)


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    l_i, r_i = 0, 0

    for g_i in range(start, end):
        if l_i >= len(left):
            numbers[g_i] = right[r_i]
            r_i = r_i + 1
        elif r_i >= len(right):
            numbers[g_i] = left[l_i]
            l_i = l_i + 1
        elif left[l_i] < right[r_i]:
            numbers[g_i] = left[l_i]
            l_i = l_i + 1
        else:
            numbers[g_i] = right[r_i]
            r_i = r_i + 1
