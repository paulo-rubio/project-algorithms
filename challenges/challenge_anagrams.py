def is_anagram(first_string, second_string):
    firstString = str(first_string)
    secondString = str(second_string)
    if len(firstString) != len(secondString):
        return False
    if (len(firstString) == 0 or len(secondString) == 0):
        return False

    sorted_first = merge_sort(list(firstString))
    sorted_second = merge_sort(list(secondString))

    for i in range(len(sorted_first)):
        if sorted_first[i] != sorted_second[i]:
            return False

    return True


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged